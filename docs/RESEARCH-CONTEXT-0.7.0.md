# Research context for 0.7.0

The 0.7.0 analyses are deliberately narrower than decipherment.

Brent Davis's 2026 chapter *Linear A Morphology* reports a refined statistical
approach to signs concentrated at word beginnings and endings and discusses
possible prefix/suffix interpretations. That makes source-defined positional
analysis an especially important comparison target. This project does not
inherit Davis's linguistic interpretation: it reports sign-position
enrichment first and stores any morphological interpretation separately.

A contemporary Linear A workbench also advertises word frequency, graphotactic
transitions, positional analysis, stem families and minimal pairs. Therefore
0.7.0 does not claim novelty merely for computing these classes of statistic.
Its research contribution target is provenance-controlled reproduction over
the independently decoded SigLA Word objects, explicit uncertainty/licensing,
context portability, null models, and separation of observation from
interpretation.

Other contemporary computational projects make stronger language-family and
translation claims. Those are not adopted here. 0.7.0 contains no
language-family scoring and no semantic translation layer.
