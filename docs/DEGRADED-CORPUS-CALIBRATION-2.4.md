# 2.4 — Preregistered degraded-corpus calibration

## Question
How rapidly does a detector measured on deciphered Linear B lose structural recovery when the observable corpus is degraded toward Linear-A-like evidence conditions?

## Gate
2.4 is not executable as a scored calibration until 2.3 has produced an authenticated undegraded blind baseline and the gold-scoring contract has been frozen. Synthetic degradation is not a substitute for that baseline.

## Frozen degradation dimensions
1. **Document/token scale.** Select whole Linear B documents, not independent words, using seeded subset optimization that minimizes absolute distance from 1,283 tokens.
2. **Recurrence.** Report type/hapax/recurrent structure and reject grossly mismatched samples; never relabel Linear B words to manufacture a match.
3. **Damage.** Independently mask signs at 0%, 5%, 10%, and 20%. Track boundary and internal masking separately. Fully masked words are explicitly counted as missing outcomes and are never silently removed from denominator diagnostics.
4. **Combined conditions.** Compare undegraded, scale-only, damage-only, and scale+damage conditions.

Each condition uses 1,000 deterministic replicates from master seed 2400001.

## Linear A empirical targets
The preregistration uses the canonical source-word table: 1,283 nonempty tokens in 451 represented documents, 836 distinct types, 668 hapax types, and 168 recurrent types. These are evidence-distribution targets, not linguistic claims.

## Interpretation
2.4 measures sensitivity to modeled evidence loss. It cannot establish affixes, morphemes, readings, language identity, or decipherment. A detector that survives modeled degradation is robust to those modeled conditions only.
