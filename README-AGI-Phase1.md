# DOG2 Prognosis Predictor — AGI Phase 1, v0.3 (2026-10-26)

Based on the original working `dog2-all56-pwa-main.zip` provided by AGI.

## What was changed
- Official AGI dog logo (transparent supplied artwork), extracted official colors `#006A32` and `#318C2C`.
- Friendly cream-and-green Shiny user interface; small paw-print decorations; mobile responsive CSS.
- Dedicated Dog + Human Evidence page reporting the prior frozen DOG2→TARGET evaluation results.
- About AGI, interpretation, model/privacy, install pages.
- Green AGI dog PWA icons and theme; simple label update on prediction PDF.

## Crucial: what was NOT changed
The frozen prediction model, 56 gene set definitions, canine/human map, scoring and QC logic, R download handlers, Shinylive runtime, and iOS TSV/PDF workarounds are retained from the supplied archive. `server <- function(...)` is unchanged except the generated PDF's title styling.

## Deploy
This folder is a **pre-exported Shinylive static site**: publish *the contents of this folder* to the repository's GitHub Pages root. Test first on a separate branch or test repo. Then visit the Pages URL, clear or reload prior PWA versions as needed, and test desktop + iPhone. Do not overwrite your working public Pages app before parity checks.

To serve locally:

```bash
python3 -m http.server 8000
```

Open http://localhost:8000/ (browser must support WebAssembly and service workers).

## Before public release
1. Run real sample prediction and compare frozen DFI/OS scores/percentiles and mapping QC to old app; use `validate_shinylive_parity.R` and locked sample gold standard if available.
2. Test actual PDF/TSV download on iPhone in standalone mode.
3. Confirm the frozen model `.rds` and gene mapping may be publicly distributed: **static webR apps make these files downloadable**.
4. Check reported TARGET OS C-index=0.709 (n=81, 29 events; p=0.00399), EFS C-index=0.608 (n=80, 41 events; p=0.083), HRs and the OS PH-test p=0.020 against frozen final 10e5 study output prior to public release.
5. The UI accepts human gene symbols for *exploratory* scoring, but no individual human prognosis is clinically validated.
6. When publishing to GitHub Pages, avoid committing sample expression data containing sensitive identifiers.

## Source
Original AGI logo: user-supplied `AGI_logo_transparent.png`. Official colors sampled from image. No third-party image dependencies.
