"""Kontrollér den faktiske PDF og log; fejler ved manglende navigation eller layoutadvarsler."""
import sys
from pathlib import Path
import fitz
pdf, log = map(Path, sys.argv[1:])
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
    assert len(doc) >= 15, 'Uventet kort kompendium'
    assert len(toc) >= 80, 'Kapitler eller PDF-bogmærker mangler'
    assert links >= 80, 'Klikbar navigation mangler'
    for heading in ['Differentialregning', 'Taylorudvikling', 'Numerisk differentiation', 'Greenfunktioner']:
        assert heading in contents, f'Mangler: {heading}'
    assert '\ufffd' not in contents, 'Ugyldige teksttegn i PDF'
    print(f'PDF: {len(doc)} sider, {len(toc)} bogmærker, {links} links.')
if problems:
    raise SystemExit('\n'.join(problems))
print('Ingen overfyldte bokse, manglende tegn eller uafklarede referencer i loggen.')
