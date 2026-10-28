# DOG2–AGI PWA: pre-release checklist

- [ ] Confirm that it is acceptable to publish the frozen model + gene mapping embedded in `app.json`.
- [ ] Verify `python3 verify_site.py` succeeds.
- [ ] Compare DFI and OS score, training percentile, QC and gene mapping for one or more fixed input files against the original DOG2 app.
- [ ] Confirm all three gene identifier choices: canine Ensembl ID, canine gene symbol and human gene symbol.
- [ ] Confirm low-coverage / malformed input receives accurate QC failure or warning.
- [ ] Test PDF and TSV downloads on desktop, mobile Safari and installed standalone iPhone PWA.
- [ ] Review TARGET metrics against the final frozen analysis output. TARGET OS finding is exploratory transfer evidence; do not imply clinical validation or calibrated survival probability.
- [ ] Confirm no sample-level protected data or private credentials are committed.
- [ ] Confirm URL resolves under `/dog2-agi-predictor/`, install works, and home-screen icon is recognizable.
- [ ] Check source acknowledgements, AGI branding, research-only disclaimer and contact link.
