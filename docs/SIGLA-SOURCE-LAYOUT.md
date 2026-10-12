# Source-bound SigLA layout evidence

`research/sigla-source-layout.json` retains 5,144 source rectangles across 802 SigLA document views, including the source image-plane size and raw reading/erasure/ghost flags. This is newly exposed layout information from the existing source snapshot, not 802 new inscriptions or newly accepted readings. Source data and derived layout retain **CC BY-NC-SA 4.0**, attributed to Ester Salgarella and Simon Castellan; source drawings are not bundled.

The current [SigLA dataset](https://sigla.phis.me/database.js) was acquired through ordinary HTTP on 2026-10-12. Its SHA-256 is identical to the upstream SHA recorded in the frozen derivative. The [source terms](https://sigla.phis.me/about.html) explicitly cover the dataset and drawings. The published application serializers and SVG renderer establish the rectangle order `x,y,w,h` and document `image_size`; they do not establish physical measurements. Coordinates stay in the source drawing/image plane. No image was downloaded, and no GORILA edition was accessed or reconstructed.

Two distinct Marshal readers agree on all document image sizes and all 5,144 rectangles. A replay of the current derivative-exporter mapping gives 5,143 exact attestation projections and one difference at HT 6a, zero-based source-array slot 11. It differs in `sign`/`kind` interpretation despite identical upstream bytes. Both projections and the code/source hashes are retained in `research/sigla-layout-source-inspection.json`; the existing reading is not silently corrected. This is exporter dependence, not independent epigraphic confirmation or a newly changed ancient source.

Source array indices, source record numbers and canonical sign numbers are distinct. The legacy normalization helper's record-number projection must not be used as a canonical sign-number concordance. The layout layer uses document keys and source-array lineage; it admits no new sign identification, phonetic value, damaged-sign diagnosis or physical identity. Raw reading constructors and flags remain uninterpreted. Source drawings and their editorial ancestry remain dependent evidence.

Run the source-bound replay and integrity checks:

```sh
python scripts/build_sigla_layout_layer.py /path/to/database.js
python scripts/build_sigla_layout_layer.py
python -m unittest discover -s scripts -p test_sigla_layout_layer.py
python scripts/research_api.py layout --id 'HT 6a' --limit 1
```

The acquisition pin rejects changed source bytes. Validation rejects missing slots, duplicate/orphan document keys, altered source bindings, noninteger coordinates and out-of-plane rectangles; it never clips source coordinates to manufacture an acceptable layout. New upstream versions require a fresh explicit audit. Glyph interpretation and physical metrology still require appropriate evidence and scientific review.
