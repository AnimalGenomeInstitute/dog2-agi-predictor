#!/usr/bin/env python3
"""Structural check for independent AGI PWA GitHub Pages release. No model run."""
import base64
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
required = [
    '.nojekyll', 'index.html', 'app.json', 'manifest.webmanifest',
    'shinylive-sw.js', 'shinylive/shinylive.js',
    'shinylive/load-shinylive-sw.js', 'shinylive/webr/R.bin.wasm',
    'icons/icon-192.png', 'icons/icon-512.png', 'icons/apple-touch-icon.png'
]
missing = [p for p in required if not (root/p).is_file()]
if missing:
    raise SystemExit('MISSING FILES: ' + ', '.join(missing))

app = json.loads((root/'app.json').read_text(encoding='utf-8'))
files = {x['name']: x['content'] for x in app}
expected = {
    'assets/dog_human_mapping.rds': '062d5cd7f2d7d8ebd0a4ce8e3f7d8b8b2469d9d2cb1882cdcaabd995e0e6a843',
    'assets/shinylive_model_bundle.rds': 'b1f50fba7e60c58840dc2b9313d1a11ef51df513d91b23639dc89a4fb757884b',
}
for name, sha in expected.items():
    if name not in files:
        raise SystemExit('MISSING BUNDLED ASSET: '+name)
    data = base64.b64decode(files[name])
    got = hashlib.sha256(data).hexdigest()
    if got != sha:
        raise SystemExit(f'ASSET MISMATCH: {name}: {got}')
for name in ['app.R','backend_shinylive.R','www/app.css','www/paw.svg','www/agi-official-logo.png','www/pdf-overlay.js','www/tsv-share.js']:
    if name not in files:
        raise SystemExit('MISSING APP ENTRY: ' + name)
manifest = json.loads((root/'manifest.webmanifest').read_text())
if manifest.get('start_url') != './' or manifest.get('scope') != './':
    raise SystemExit('Manifest paths are not repository-relative')
if 'relPath: ""' not in (root/'index.html').read_text():
    raise SystemExit('Unexpected Shinylive relative path setting')
print(f'PASS: {len(required)} static entry files, {len(files)} Shinylive entries, '
      'unchanged bundled DOG2 model and gene mapping, relative PWA paths.')
print('NOTE: this does not execute webR/R predictions; perform real browser and model-parity tests.')
