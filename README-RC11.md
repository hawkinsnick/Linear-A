# Linear A Open Corpus — 0.4.0-rc11-local

RC11 classifies every corpus-wide violation of RC10's candidate f3 coordinate
model rather than discarding the anomalies.

Candidate groups: 1708
Structurally clean (unique, zero-based, contiguous positions): 1359
Anomalous: 349
Clean fraction: 79.6%

Of the anomalous groups, 314 coincide with at least one
explicit data condition (unreadable, doubtful, erasure, ghost, flag5, or mixed
wrapped/direct shape). **Coincidence is not treated as causation.**
35 anomalous groups have none of those conditions.

The coordinate model is therefore **not promoted**.

RC11 exports anomaly-class counts, residual unexplained cases, wrapped/direct
anomaly rates, and duplicate-coordinate structural subtypes. No coordinates are
silently repaired and no source-defined group is called a linguistic word.

Nothing has been published to GitHub. Raw SigLA data and the complete
attestation table are not bundled.
