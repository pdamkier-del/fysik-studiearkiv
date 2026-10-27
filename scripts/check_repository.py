"""Offline Markdown links, LaTeX imports/references and architecture checks."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
COURSES = {'analytisk-mekanik', 'elektromagnetisme'}
LIBRARY = {'statistik', 'klassisk-mekanik', 'elektromagnetisme', 'termodynamik',
           'statistisk-fysik', 'kvantemekanik', 'relativitet-og-gravitation',
           'optik-og-boelger', 'atom-og-molekylefysik', 'kerne-og-partikelfysik',
           'faststoffysik', 'numeriske-metoder'}
MATH = ROOT / '00-matematik/main.tex'
STATISTICS = ROOT / '02-fysikbibliotek/statistik/main.tex'


def latex_text(path):
    # Source comments are not import or reference declarations.
    return '\n'.join(line.split('%', 1)[0] for line in path.read_text().splitlines())


def latex_tree(path, stack=()):
    if path in stack:
        raise ValueError(f'Cyclic LaTeX input: {path.relative_to(ROOT)}')
    text = latex_text(path)
    sources = {path: text}
    for name in re.findall(r'\\input\{([^}]+)\}', text):
        target = ROOT / (name if name.endswith('.tex') else name + '.tex')
        if not target.is_file():
            raise ValueError(f'Missing LaTeX input: {name}')
        sources.update(latex_tree(target, (*stack, path)))
    return sources


def main(require_drive_disabled=False):
    courses = {p.name for p in (ROOT / '01-universitetsfag').iterdir() if p.is_dir()}
    library = {p.name for p in (ROOT / '02-fysikbibliotek').iterdir() if p.is_dir()}
    if courses != COURSES or library != LIBRARY:
        raise ValueError('Unexpected course or library structure')
    chapters = re.findall(r'\\input\{([^}]+/chapters/[^}]+)\}', MATH.read_text())
    if len(chapters) != 21 or len(set(chapters)) != 21 or any('statistik' in p for p in chapters):
        raise ValueError('Mathematics must have 21 distinct main topics and no statistics')
    templates = json.loads((ROOT / 'config/latex-templates.json').read_text())['sources']
    if len(templates) != 20 or len(set(templates)) != 20:
        raise ValueError('Original physics-template build targets not retained')
    all_sources = set()
    for entry in [MATH, STATISTICS, *(ROOT / p for p in templates), ROOT / '90-faelles/latex/dokumentskabelon.tex']:
        sources = latex_tree(entry)
        all_sources.update(sources)
        text = '\n'.join(sources.values())
        labels = re.findall(r'\\label\{([^}]+)\}', text)
        refs = re.findall(r'\\(?:ref|eqref|pageref|nameref)\{([^}]+)\}', text)
        if len(labels) != len(set(labels)) or set(refs) - set(labels):
            raise ValueError(f'Invalid labels/references in {entry.relative_to(ROOT)}')
    markdown = [p for base in ['00-matematik', '01-universitetsfag', '02-fysikbibliotek', '90-faelles', '99-kilder-og-pensum', 'docs'] for p in (ROOT / base).rglob('*.md')]
    markdown += list(ROOT.glob('*.md'))
    link_count = 0
    for source in markdown:
        text = re.sub(r'```.*?```', '', source.read_text(), flags=re.S)
        for raw in re.findall(r'\]\(([^)]+)\)', text):
            target = urlsplit(raw)
            if target.scheme or target.netloc or not target.path:
                continue
            resolved = (source.parent / unquote(target.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                raise ValueError(f'Broken local link in {source.relative_to(ROOT)}: {raw}')
            if target.fragment and resolved.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+)$', resolved.read_text(), flags=re.M)
                slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                if unquote(target.fragment) not in slugs:
                    raise ValueError(f'Broken heading link: {raw}')
            link_count += 1
    manifest = json.loads((ROOT / 'config/pdf-publication.json').read_text())
    for document in manifest['documents']:
        valid_subjects = {'00-matematik'} | {'01-universitetsfag/' + item for item in COURSES} | {'02-fysikbibliotek/' + item for item in LIBRARY}
        if document['subject'] not in valid_subjects:
            raise ValueError('Publication subject not migrated')
        for field in ['pdf', 'log']:
            if not document[field].startswith('build/' + document['subject'] + '/'):
                raise ValueError('Artifact destination not migrated')
        if not isinstance(document['approved'], bool):
            raise ValueError('Publication approval must be a boolean')
        if require_drive_disabled and document['approved'] is not False:
            raise ValueError('Drive publication must remain disabled during this migration')
    originals = (ROOT / 'docs/originaler.md').read_text()
    for file_id in ['1D0pjoV7JmySzJWmegeGOnvZoLxPrMQNA', '1YjrsA63LHS96ShigE7u1i7_kU2zDjO4e']:
        if file_id not in originals:
            raise ValueError('Stable original Drive ID lost')
    print(f'Architecture OK; {len(all_sources)} LaTeX sources/imports and references; {link_count} local Markdown links checked. No network requests.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-drive-disabled', action='store_true')
    main(parser.parse_args().require_drive_disabled)
