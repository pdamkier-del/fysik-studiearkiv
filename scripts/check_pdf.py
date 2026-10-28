"""Kontrollér den faktiske PDF og log; fejler ved manglende navigation eller layoutadvarsler."""
from pathlib import Path
import fitz
import argparse
import re
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('pdf', type=Path)
parser.add_argument('log', type=Path)
parser.add_argument('--bind', type=int, choices=range(1, 7))
args = parser.parse_args()
pdf, log = args.pdf, args.log
volume_headings = {
    1: ['Algebra og funktioner', 'Trigonometri', 'Lineær algebra'],
    2: ['Differentialregning', 'Integralregning', 'Flervariabel analyse'],
    3: ['Ordinære differentialligninger', 'Partielle differentialligninger', 'Sturm'],
    4: ['Komplekse tal', 'Laplacetransformationer', 'Specialfunktioner', 'Numeriske metoder'],
    5: ['Analytisk geometri', 'Vektoranalyse', 'Tensorregning', 'Differentialgeometri'],
    6: ['Variationsregning', 'Gruppeteori'],
}
text = log.read_text(errors='replace')
problems = [line for line in text.splitlines() if any(s in line for s in (
    'Overfull \\hbox', 'Overfull \\vbox', 'Missing character:',
    'LaTeX Warning: Reference', 'There were undefined references',
    'multiply defined', 'does not contain requested',
))]
with fitz.open(pdf) as doc:
    contents = '\n'.join(page.get_text() for page in doc)
    toc = doc.get_toc()
    links = sum(len(page.get_links()) for page in doc)
    for page in doc:
        for link in page.get_links():
            if link['kind'] == fitz.LINK_GOTO:
                assert 0 <= link['page'] < len(doc), 'Ugyldig intern linkdestination'
    for _, _, page_number in toc:
        assert 1 <= page_number <= len(doc), 'Ugyldigt bogmærke'
    assert len(doc) >= (4 if args.bind else 15), 'Uventet kort kompendium'
    assert len(toc) >= (8 if args.bind else 80), 'Kapitler eller PDF-bogmærker mangler'
    assert links >= (8 if args.bind else 80), 'Klikbar navigation mangler'
    headings = volume_headings[args.bind] if args.bind else [
        'Differentialregning', 'Taylorudvikling', 'Numerisk differentiation', 'Greenfunktioner']
    for heading in headings:
        assert heading in contents, f'Mangler: {heading}'
    if args.bind == 1:
        # Check both printed page labels and actual destinations, including
        # formulas adjacent to a page break (the two can otherwise disagree).
        entries = re.findall(
            r'\\contentsline \{section\}.*?\{(\d+)\}\{(equation\.[^}]+)\}',
            pdf.with_suffix('.for').read_text())
        expected = {destination: page for page, destination in entries}
        assert len(entries) == len(expected) >= 60, 'Formelregisterposter mangler'
        start = next(page - 1 for _, title, page in toc if title == 'Formelregister')
        found = set()
        for page in list(doc)[start:]:
            for link in page.get_links():
                destination = link.get('nameddest')
                if destination not in expected:
                    continue
                target = doc[link['page']]
                assert target.get_label() == expected[destination], (
                    f'Forkert sidetal i formelregister: {destination}')
                assert destination.removeprefix('equation.') in target.get_text(), (
                    f'Formelnummer mangler ved destination: {destination}')
                found.add(destination)
        assert found == set(expected), 'Formelregisterlinks mangler'
        print(f'Formelregister: {len(found)} links og trykte sidetal kontrolleret.')
    assert '\ufffd' not in contents, 'Ugyldige teksttegn i PDF'
    print(f'PDF: {len(doc)} sider, {len(toc)} bogmærker, {links} links.')
if problems:
    raise SystemExit('\n'.join(problems))
print('Ingen overfyldte bokse, manglende tegn eller uafklarede referencer i loggen.')
