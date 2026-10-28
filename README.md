# DOG2 Prognosis Predictor — Animal Genome Institute 🐾

**Independent AGI app repository (Phase 1 / v0.3).** This repository is a separate copy of the DOG2 PWA, based on the AGI Phase 1 build. It does **not** require or modify `dog2-all56-pwa`.

- **Predict**: frozen DOG2 56-signature research model for DFI and OS relative-risk scores, with QC and TSV/PDF exports.
- **Evidence**: dog model background and exploratory human TARGET transfer evaluation.
- **Branding**: official AGI dog logo, AGI green, paw motif; installable PWA.
- **Technology**: self-contained static Shinylive/webR website; no Shiny compute server.

This is a **research-only** predictor, not a validated clinical diagnostic or individualized recurrence/mortality probability calculator.

## Start here

- [日本語：新しいGitHubリポジトリの作り方](SETUP_NEW_REPOSITORY_JA.md)
- [Checklist before making public](PUBLIC_RELEASE_CHECKLIST.md)
- [Phase 1 design / technical notes](README-AGI-Phase1.md)

## Run on a laptop before publishing

Open a terminal **in this folder**, then:

```bash
python3 -m http.server 8000
```

Open <http://localhost:8000/>. Do not open `index.html` directly from Finder (`file://`), because the browser-based R runtime and service worker need an HTTP origin.

For a simple structural preflight:

```bash
python3 verify_site.py
```

## GitHub Pages

On a **brand-new** GitHub repo called `dog2-agi-predictor`, place everything in this folder at repository **root**, not within an extra nested folder. Then: **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**.

After publication, the intended URL is:

`https://<your-github-username>.github.io/dog2-agi-predictor/`

The `./` paths and manifest scope support this repository-specific URL. The old `dog2-all56-pwa` site stays independent.

## Public release warning

**Inspect the privacy and redistribution status of `app.json` before publishing.** The static `app.json` includes the frozen model and dog↔human gene mapping RDS assets, which visitors can retrieve. If these must remain confidential, do *not* make this repository public or publish on GitHub Pages; use a server-based alternative. Do not commit confidential sample-level expression files or identifiers.

Also independently verify sample prediction parity with the original app, mobile PDF/TSV export, and TARGET study statistics before describing the result as validated.

Copyright and ownership: AGI supplied the logo and DOG2 model. This package does not assert a new software license.
