"""Checks locais do perfil Spec Foundry 1.0; não é um engine universal JSON Schema."""
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

SKILL_ROOT = Path(__file__).resolve().parents[1]
CORE = [
    'README.md', 'AGENTS.md', 'CLAUDE.md', 'model/project-model.json',
    'schemas/project-model.schema.json', 'evals/cases.json', 'evals/eval-spec.md', 'evals/rubrics.md',
    'docs/specs/01-product-spec.md', 'docs/specs/02-requirements.md',
    'docs/specs/03-system-design.md', 'docs/specs/04-implementation-plan.md',
    'docs/specs/05-agent-configuration.md', 'docs/domain-model.md', 'docs/data-contracts.md',
    'docs/traceability.md', 'docs/open-questions.md', 'docs/assumptions-and-risks.md',
    'docs/review.md', 'docs/change-impact.md',
]
LIMITATIONS = [
    'Somente o subconjunto de JSON Schema usado no contrato fornecido e invariantes locais.',
    'Não executa OCR/visão, retrieval, pesquisa web, avaliação LLM ou testes do sistema-alvo.',
    'Não comprova sustentação semântica, identidade humana, autenticidade ou validação regulatória.',
    'Arquivos e registros declarativos podem ser editados; hashes não são assinaturas.',
]


def load(path):
    def invalid_constant(value):
        raise ValueError('Número JSON inválido: ' + value)
    return json.loads(Path(path).read_text(encoding='utf-8'), parse_constant=invalid_constant)


def dump(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def digest(path):
    with Path(path).open('rb') as f:
        h = hashlib.sha256()
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def safe_path(root, name, exists=True):
    if not isinstance(name, str) or not name or '\\' in name or '\x00' in name:
        raise ValueError('Caminho vazio/inválido')
    p = PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or name.startswith('./'):
        raise ValueError('Caminho absoluto/traversal não permitido: ' + name)
    current = root
    for part in p.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError('Symlink não permitido: ' + name)
    if not current.resolve().is_relative_to(root.resolve()):
        raise ValueError('Caminho fora do projeto: ' + name)
    if exists and (not current.is_file() or current.stat().st_size == 0):
        raise ValueError('Arquivo ausente/vazio: ' + name)
    return current


def check_schema(value, schema, contract, path='$'):
    """Suporta somente keywords presentes no schema fornecido; erro em keyword desconhecida."""
    supported = {'$schema', '$id', 'title', '$defs', '$ref', 'type', 'required', 'properties',
                 'additionalProperties', 'items', 'minItems', 'maxItems', 'uniqueItems',
                 'minLength', 'pattern', 'enum', 'minimum', 'maximum'}
    unknown = set(schema) - supported
    if unknown:
        raise ValueError(f'{path}: keywords não suportadas {sorted(unknown)}')
    if '$ref' in schema:
        target = schema['$ref']
        if not target.startswith('#/$defs/'):
            raise ValueError(f'{path}: referência de schema não local')
        return check_schema(value, contract['$defs'][target.split('/')[-1]], contract, path)
    kinds = schema.get('type', [])
    if isinstance(kinds, str):
        kinds = [kinds]
    predicates = {
        'null': value is None, 'boolean': isinstance(value, bool),
        'integer': isinstance(value, int) and not isinstance(value, bool),
        'number': isinstance(value, (int, float)) and not isinstance(value, bool),
        'string': isinstance(value, str), 'array': isinstance(value, list), 'object': isinstance(value, dict),
    }
    if kinds and not any(predicates.get(k, False) for k in kinds):
        raise ValueError(f'{path}: tipo inválido; esperado {kinds}')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{path}: valor fora do enum')
    if isinstance(value, dict):
        missing = set(schema.get('required', [])) - set(value)
        if missing:
            raise ValueError(f'{path}: campos ausentes {sorted(missing)}')
        properties = schema.get('properties', {})
        if schema.get('additionalProperties') is False and set(value) - set(properties):
            raise ValueError(f'{path}: campos não previstos {sorted(set(value)-set(properties))}')
        for key, item in value.items():
            if key in properties:
                check_schema(item, properties[key], contract, f'{path}.{key}')
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0) or len(value) > schema.get('maxItems', float('inf')):
            raise ValueError(f'{path}: quantidade de itens inválida')
        if schema.get('uniqueItems') and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            raise ValueError(f'{path}: itens duplicados')
        for index, item in enumerate(value):
            check_schema(item, schema.get('items', {}), contract, f'{path}[{index}]')
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0):
            raise ValueError(f'{path}: texto vazio/curto')
        if 'pattern' in schema and re.search(schema['pattern'], value) is None:
            raise ValueError(f'{path}: padrão inválido')
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < schema.get('minimum', -float('inf')) or value > schema.get('maximum', float('inf')):
            raise ValueError(f'{path}: fora dos limites')


def validate(root, exported=False):
    root = Path(root).resolve()
    errors, warnings = [], []
    model = None
    try:
        model = load(safe_path(root, 'model/project-model.json'))
        schema = load(SKILL_ROOT/'schemas/project-model.schema.json')
        project_schema = load(safe_path(root, 'schemas/project-model.schema.json'))
        if project_schema != schema:
            raise ValueError('Schema local difere do contrato da skill; migração/revisão explícita necessária')
        check_schema(model, schema, schema)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        return {'structural_status': 'fail', 'errors': [str(exc)], 'warnings': [], 'limitations': LIMITATIONS}

    def require(test, message):
        if not test:
            errors.append(message)

    def file(name):
        try:
            return safe_path(root, name)
        except (ValueError, OSError) as exc:
            errors.append(str(exc))
            return None

    indexes = {}
    groups = ['sources', 'evidence', 'claims', 'requirements', 'decisions', 'tasks', 'risks', 'questions', 'conflicts', 'eval_cases']
    all_ids = []
    for group in groups:
        indexes[group] = {item['id']: item for item in model[group]}
        all_ids.extend(item['id'] for item in model[group])
    require(len(all_ids) == len(set(all_ids)), 'IDs duplicados')
    require(bool(model['requirements']), 'Falta ao menos um requisito substantivo')
    require(bool(model['sources']), 'Falta ao menos uma fonte do projeto')

    def refs(values, group, owner):
        for value in values:
            require(value in indexes[group], f'{owner}: referência não resolvida {value}')

    def human(eid, owner):
        ev = indexes['evidence'].get(eid)
        require(ev is not None, f'{owner}: evidência humana ausente')
        if ev:
            src = indexes['sources'].get(ev['source_ref'], {})
            require(src.get('kind') == 'user_message' and ev['quality'] == 'clear' and bool(ev['quote']),
                    f'{owner}: autorização/resposta precisa de mensagem humana clara e citada')

    omitted_sources = set()
    if exported:
        try:
            manifest = load(safe_path(root, 'manifest.json'))
            require(manifest.get('project_id') == model['project_id'] and manifest.get('revision') == model['revision'] and manifest.get('scope') == model['scope'], 'Manifest não corresponde ao projeto/revisão/escopo')
            require(manifest.get('private_original_sources_included') is False, 'Exportado precisa declarar exclusão dos originais')
            entries = manifest.get('files', [])
            require(len(entries) == len({e['path'] for e in entries}), 'Manifest com arquivos duplicados')
            require({e['path'] for e in entries} == {a['path'] for a in model['artifacts']}, 'Manifest diverge dos artefatos do modelo')
            for entry in entries:
                p = file(entry['path'])
                if p:
                    require(digest(p) == entry['sha256'] and p.stat().st_size == entry['bytes'], 'Hash/tamanho exportado incorreto: ' + entry['path'])
            for source in model['sources']:
                if source['local_path']:
                    candidate = safe_path(root, source['local_path'], exists=False)
                    if not candidate.exists():
                        omitted_sources.add(source['id'])
                        warnings.append(source['id'] + ': original privado ausente; hash/citação não verificáveis no exportado')
        except (ValueError, KeyError, TypeError, OSError) as exc:
            errors.append('Manifest exportado inválido: ' + str(exc))

    for source in model['sources']:
        require(bool(source['local_path']) == bool(source['sha256']), f"{source['id']}: arquivo/hash devem vir juntos")
        if source['local_path'] and source['id'] not in omitted_sources:
            p = file(source['local_path'])
            if p:
                require(digest(p) == source['sha256'], f"{source['id']}: hash de origem incorreto")
    for ev in model['evidence']:
        refs([ev['source_ref']], 'sources', ev['id'])
        locator = ev['locator']
        if locator['kind'] == 'text_lines':
            lines = locator.get('lines', [])
            require(len(lines) == 2 and lines[0] <= lines[1], f"{ev['id']}: intervalo de linhas inválido")
        if locator['kind'] == 'pdf_page':
            require('page' in locator, f"{ev['id']}: página PDF obrigatória")
        if locator['kind'] == 'image_region':
            box = locator.get('bbox', [])
            require(len(box) == 4 and box[0] < box[2] and box[1] < box[3], f"{ev['id']}: bbox inválido")
        source = indexes['sources'].get(ev['source_ref'], {})
        if source.get('local_path') and source.get('kind') in ('text', 'user_message') and source.get('id') not in omitted_sources:
            p = file(source['local_path'])
            if p:
                try:
                    content = p.read_text(encoding='utf-8')
                    if locator['kind'] == 'text_lines' and len(locator.get('lines', [])) == 2:
                        a, b = locator['lines']
                        require(b <= len(content.splitlines()), f"{ev['id']}: linhas fora do texto")
                        content = '\n'.join(content.splitlines()[a-1:b])
                    if ev['quote']:
                        require(ev['quote'] in content, f"{ev['id']}: citação não encontrada no trecho")
                except UnicodeError:
                    errors.append(f"{ev['id']}: texto local não é UTF-8")
        elif source.get('kind') in ('pdf', 'image', 'web', 'mcp'):
            warnings.append(f"{ev['id']}: fonte {source.get('kind')} exige revisão semântica/ferramenta específica")
    for claim in model['claims']:
        refs(claim['evidence_refs'], 'evidence', claim['id'])
        if claim['kind'] != 'proposal':
            require(bool(claim['evidence_refs']), f"{claim['id']}: claim factual sem evidência")
    for decision in model['decisions']:
        refs(decision['requirement_refs'], 'requirements', decision['id'])
        if decision['evidence_ref']:
            refs([decision['evidence_ref']], 'evidence', decision['id'])
        if decision['status'] == 'approved':
            human(decision['evidence_ref'], decision['id'])
    blockers = []
    for req in model['requirements']:
        refs(req['claim_refs'], 'claims', req['id'])
        refs(req['decision_refs'], 'decisions', req['id'])
        if req['status'] != 'deferred':
            require(bool(req['claim_refs']), f"{req['id']}: requisito ativo sem claim")
            linked = [ev for ev in model['eval_cases'] if req['id'] in ev['requirement_refs'] and ev['layer'] == 'target_system']
            require(bool(linked), f"{req['id']}: sem eval target_system")
            require(any(req['id'] in task['requirement_refs'] for task in model['tasks']), f"{req['id']}: sem tarefa")
            if req['priority'] == 'critical':
                require(any(ev['severity'] == 'critical' for ev in linked), f"{req['id']}: falta eval crítica")
            for cid in req['claim_refs']:
                for eid in indexes['claims'].get(cid, {}).get('evidence_refs', []):
                    if indexes['evidence'].get(eid, {}).get('quality') == 'uncertain':
                        blockers.append(f"{req['id']}: evidência incerta {eid}")
        if req['status'] == 'accepted':
            valid = [indexes['decisions'].get(d, {}) for d in req['decision_refs']]
            require(any(d.get('status') == 'approved' and d.get('revision') == model['revision'] and d.get('scope') == model['scope'] and req['id'] in d.get('requirement_refs', []) for d in valid), f"{req['id']}: aceitação sem decisão aprovada na mesma revisão/escopo")
    for task in model['tasks']:
        refs(task['requirement_refs'], 'requirements', task['id'])
        refs(task['dependency_refs'], 'tasks', task['id'])
    visited, visiting = set(), set()
    def visit(tid):
        if tid in visiting:
            errors.append(f'Dependência cíclica: {tid}')
            return
        if tid in visited or tid not in indexes['tasks']:
            return
        visiting.add(tid)
        for dep in indexes['tasks'][tid]['dependency_refs']:
            visit(dep)
        visiting.remove(tid)
        visited.add(tid)
    for tid in indexes['tasks']:
        visit(tid)
    for risk in model['risks']:
        refs(risk['requirement_refs'], 'requirements', risk['id'])
    for question in model['questions']:
        if question['blocking'] and question['status'] != 'answered':
            blockers.append(question['id'])
        if question['status'] == 'answered':
            human(question['evidence_ref'], question['id'])
        elif question['evidence_ref']:
            refs([question['evidence_ref']], 'evidence', question['id'])
    for conflict in model['conflicts']:
        refs(conflict['claim_refs'], 'claims', conflict['id'])
        require(len(conflict['claim_refs']) >= 2, f"{conflict['id']}: conflito exige duas claims")
        if conflict['blocking'] and conflict['status'] == 'open':
            blockers.append(conflict['id'])
        if conflict['status'] == 'resolved':
            human(conflict['resolution_evidence_ref'], conflict['id'])
    for case in model['eval_cases']:
        refs(case['requirement_refs'], 'requirements', case['id'])
        if case['fixture_status'] == 'missing':
            require(case['fixture_ref'] is None, f"{case['id']}: fixture missing deve ter ref null")
        else:
            require(case['fixture_ref'] is not None, f"{case['id']}: fixture precisa de arquivo")
            if case['fixture_ref']:
                file(case['fixture_ref'])
        if case['execution_status'] in ('passed', 'failed'):
            require(bool(case['executor']) and bool(case['report_ref']), f"{case['id']}: resultado sem executor/relatório")
            if case['report_ref']:
                p = file(case['report_ref'])
                if p:
                    try:
                        report = load(p)
                        require(report.get('layer') == case['layer'] and report.get('revision') == model['revision'] and case['id'] in report.get('case_ids', []) and report.get('status') == case['execution_status'] and report.get('executor') == case['executor'], f"{case['id']}: relatório não corresponde ao caso/camada/revisão")
                        require(bool(report.get('limitations')) and bool(report.get('evidence_refs')), f"{case['id']}: relatório sem limitações/evidências")
                        for name in report.get('evidence_refs', []):
                            file(name)
                    except (ValueError, TypeError, AttributeError):
                        errors.append(f"{case['id']}: relatório JSON inválido")
        else:
            require(case['report_ref'] is None, f"{case['id']}: não executado não deve apontar relatório")
    eval_file = file('evals/cases.json')
    if eval_file:
        try:
            require(load(eval_file) == model['eval_cases'], 'evals/cases.json diverge do modelo')
        except ValueError:
            errors.append('evals/cases.json inválido')
    require(model['readiness'] == 'discovery' or not blockers, 'Prontidão incompatível com bloqueios: ' + ', '.join(blockers))
    for review in model['semantic_reviews']:
        if review['kind'] == 'human':
            human(review['evidence_ref'], 'semantic_review')
        elif review['evidence_ref']:
            refs([review['evidence_ref']], 'evidence', 'semantic_review')
    for approval in model['approvals']:
        human(approval['evidence_ref'], 'approval')
    if model['readiness'] == 'approved_baseline':
        reviews = [r for r in model['semantic_reviews'] if r['revision'] == model['revision'] and r['scope'] == model['scope']]
        approvals = [a for a in model['approvals'] if a['revision'] == model['revision'] and a['scope'] == model['scope']]
        require(bool(approvals) and approvals[-1]['decision'] == 'approve', 'Falta aprovação vigente da baseline')
        human_reviews = [r for r in reviews if r['kind'] == 'human']
        require(bool(human_reviews) and human_reviews[-1]['result'] == 'pass', 'Falta revisão humana vigente em pass')
        require(bool(reviews) and reviews[-1]['result'] == 'pass', 'Revisão mais recente solicita alterações/falha')
    artifact_paths = [a['path'] for a in model['artifacts']]
    require(len(artifact_paths) == len(set(artifact_paths)), 'Artefatos duplicados')
    require(set(CORE) <= set(artifact_paths), 'Faltam arquivos obrigatórios no registro: ' + ', '.join(sorted(set(CORE)-set(artifact_paths))))
    for case in model['eval_cases']:
        for name in [case['fixture_ref'], case['report_ref']]:
            if name:
                require(name in artifact_paths, f"{case['id']}: fixture/relatório precisa estar registrado para export {name}")
        if case['report_ref']:
            try:
                report = load(safe_path(root, case['report_ref']))
                for name in report.get('evidence_refs', []):
                    require(name in artifact_paths, f"{case['id']}: evidência de execução não será exportada {name}")
            except (ValueError, OSError, AttributeError, TypeError):
                pass  # O erro concreto do relatório já é registrado no check do caso.
    for artifact in model['artifacts']:
        name = artifact['path']
        require(not name.startswith(('sources/', '.git/')) and name != 'manifest.json' and not any(part.startswith('.env') for part in PurePosixPath(name).parts) and Path(name).suffix.lower() not in ('.pem', '.key', '.p12', '.pfx'), 'Arquivo privado/manifest não deve ser exportado: ' + name)
        refs(artifact['requirement_refs'], 'requirements', name)
        refs(artifact['eval_refs'], 'eval_cases', name)
        p = file(name)
        if not p:
            continue
        if p.suffix in ('.md', '.json'):
            text = p.read_text(encoding='utf-8')
            require(not re.search(r'\{\{[^}]+\}\}|\[Preencher[^\]]*\]', text), 'Marcador de template não resolvido: ' + name)
            if p.suffix == '.md':
                for rid in artifact['requirement_refs'] + artifact['eval_refs']:
                    require(rid in text, f'{name}: ID registrado ausente do texto {rid}')
                without_code = re.sub(r'```.*?```', '', text, flags=re.S)
                for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', without_code):
                    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                        continue
                    clean = target.split('#')[0].replace('%20', ' ')
                    candidate = (p.parent / clean).resolve()
                    if not candidate.is_relative_to(root):
                        errors.append(f'{name}: link sai do projeto {target}')
                    elif not candidate.exists():
                        errors.append(f'{name}: link local quebrado {target}')
                    elif candidate.is_file():
                        rel = candidate.relative_to(root).as_posix()
                        file(rel)
                        require(rel in artifact_paths, f'{name}: link aponta arquivo não exportado {target}')
    requirement_doc = file('docs/specs/02-requirements.md')
    if requirement_doc:
        content = ' '.join(requirement_doc.read_text(encoding='utf-8').split())
        for req in model['requirements']:
            if req['status'] != 'deferred':
                require(req['id'] in content and ' '.join(req['statement'].split()) in content, f"{req['id']}: requisito ativo não representado textualmente no documento")
    return {'structural_status': 'fail' if errors else 'pass', 'project_id': model['project_id'], 'revision': model['revision'], 'declared_readiness': model['readiness'], 'mode': 'exported_without_private_originals' if exported else 'local_with_sources', 'blockers': blockers, 'errors': errors, 'warnings': warnings, 'limitations': LIMITATIONS}
