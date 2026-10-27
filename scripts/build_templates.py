"""Compile every retained physics template from the explicit source manifest."""
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'config/latex-templates.json').read_text())
for relative in manifest['sources']:
    source = Path(relative)
    output = Path('build') / source.parent
    (root / output).mkdir(parents=True, exist_ok=True)
    with (root / output / 'console.log').open('w') as console:
        result = subprocess.run([
            'latexmk', '-lualatex', '-interaction=nonstopmode', '-halt-on-error',
            '-file-line-error', f'-outdir={output}', str(source),
        ], cwd=root, stdout=console, stderr=subprocess.STDOUT)
    if result.returncode:
        print((root / output / 'console.log').read_text())
        raise SystemExit(result.returncode)
    log = (root / output / 'main.log').read_text(errors='replace')
    if any(item in log for item in ('Overfull', 'Missing character:', 'undefined references', 'Fatal error')):
        raise SystemExit(f'Template log failed: {source}')
    print(f'Template built: {source}')
print(f"{len(manifest['sources'])} retained template builds passed.")
