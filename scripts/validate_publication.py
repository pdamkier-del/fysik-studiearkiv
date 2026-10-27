"""Validate every declared PDF and its current build log before publication."""
import json
from pathlib import Path
import fitz


def validate(document):
    pdf, log = Path(document['pdf']), Path(document['log'])
    if not pdf.is_file() or not log.is_file():
        raise ValueError(f"Missing PDF or build log: {document['key']}")
    text = log.read_text(errors='replace')
    if 'Output written on main.pdf' not in text:
        raise ValueError('Build log does not report a successful PDF')
    failures = ['Overfull \\hbox', 'Overfull \\vbox', 'Missing character:',
                'undefined references', 'multiply defined', 'Fatal error']
    if any(item in text for item in failures):
        raise ValueError(f"Unresolved build errors: {document['key']}")
    with fitz.open(pdf) as doc:
        if doc.is_encrypted or len(doc) < document['minimum_pages']:
            raise ValueError('Encrypted or unexpectedly short PDF')
        if not doc.get_toc() or not any(p.get_links() for p in doc):
            raise ValueError('Missing PDF navigation')
        for page in doc:
            for link in page.get_links():
                if link['kind'] == fitz.LINK_GOTO and not 0 <= link['page'] < len(doc):
                    raise ValueError('Invalid internal link')
        print(f"Validated {document['key']}: {len(doc)} pages")


if __name__ == '__main__':
    for document in json.loads(Path('config/pdf-publication.json').read_text())['documents']:
        validate(document)
