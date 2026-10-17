# Specialist research-task pilots

These pilots turn proposed research uses into bounded, reproducible exercises. They are hypotheses about usefulness based on scholars' research interests, not evidence that those scholars requested, used, reviewed or endorsed the project. The gaps below describe the admitted project layers, not deficiencies in other scholars' research or tools.

| Corpus | Executed exercise | Result | What remains outside the result |
|---|---|---|---|
| [Linear B](https://github.com/hawkinsnick/Linear-B/blob/main/docs/RESEARCH-TASK-PILOT.md) | Literal `ko-wa` retrieval in 25 frozen Pylos source records | 23 literal matches; 12 after a declared whole-record character-marker screen | Name/person classification, exact linguistic word IDs, primary-edition crosswalk, person identity, calibration |
| [Linear A](../docs/RESEARCH-TASK-PILOT.md) | Exact KU RO source-label sequence within one non-null source group, across 25 frozen Haghia Triada entries | Seven matches in seven source-document entries | Phonetic/semantic interpretation, independently adjudicated word boundaries, source-collated competing readings, expert acceptance |
| [Luwian / Anatolian Hieroglyphic](https://github.com/hawkinsnick/Anatolian-Hieroglyphic/blob/main/docs/RESEARCH-TASK-PILOT.md) | Trace all seven existing edition-metadata pilot dossiers | Seven reported edition routes; zero direct-edition checks performed by this pilot | Reading-level sign study is not executed; admissible source readings, exact loci and source consultation are prerequisites |

Source records and documentary dossier counts are not unique ancient-object counts. A literal substring match is not a linguistically classified occurrence. Linear B's marker screen is not a secure-reading classifier; it may exclude an unmarked match because another part of its record contains a declared marker. All primary sources, source-specific rights, uncertainty, source dependence and native acceptance gates remain distinct.

## Start a research session

1. Choose one native walkthrough above and read its saved executed result.
2. Record the repository revision, source-file hashes, sample selection and query method. Read the upstream attribution and component rights before reuse or uploading evidence to an AI service.
3. Follow the native reproduction commands. Linear B reacquires its checksum-pinned public derivative locally; its full record results and HTML remain local by default. The public receipt includes aggregates and result/source/code hashes, not transcription payloads. Linear A uses its existing admitted public source view. Luwian uses existing bibliographic metadata only.
4. Keep the native unit and scope in the answer. Do not combine the three pilots into a pooled sign, word, inscription or witness total.
5. For AI assistance, supply the individual skill and actual evidence/result files, then use the native walkthrough prompt. Instructions and an aggregate receipt cannot substitute for unseen record-level evidence. Preserve missing fields as unknown, not zero.
6. Give a reviewer one bounded question, the exact evidence and method, and record the consulted edition/locus, expertise, conflicts, source dependence, reasoning and dissent. The current state is PREPARED_NOT_REVIEWED. No named reviewer, human acceptance or empirical model-behavior result is claimed.

## Source and interpretation progression

The next Linear B step is an admissible linguistic annotation package linked to the exact observation snapshot, together with an authoritative identifier/edition crosswalk. Source hand labels are usable as reported attributions, not newly certified palaeography. Later person-equivalence assertions require their own evidence and must remain separate from name occurrences. Never expose interpretation layers to a blinded calibration predictor.

For Linear A, a repeated source-label sequence is reproducible descriptive evidence, not a decipherment result. The separate U008 audit illustrates why attributable same-locus readings must be established before critical comparison. It is not an alternative edition of the KU RO example. The GORILA firewall remains binding.

For Luwian, establish source rights and consult an edition at a precise locus before adding reading-level sign occurrences or alternative analyses. Current identity/bibliography routes cannot support an invented sign concordance. Retain disputed dates, fragment/replica distinctions and all source lineage.

## Integration and verification

Each native repository supplies `scripts/task_pilot.py`, `scripts/test_task_pilot.py`, `analysis/task-pilot-example.json` and `docs/RESEARCH-TASK-PILOT.md`. Linear A and Linear B additionally freeze their sample/query in `research/task-pilot.json`. Individual AI authority profiles require the relevant pilot artifacts, and their bundle builders hash them. The master routes to those native resources rather than maintaining a second corpus. The instruction-only master starter includes this guide, not local Linear B source/result payloads.

The pilots have synthetic/adversarial engineering controls and executed native-data examples. Linear B's 23/12 counts were also cross-checked directly against the authenticated raw source using a separate regex calculation. This checks retrieval implementation, not epigraphy or linguistic correctness. The walkthroughs state exact reproduction and remaining scholarly work; no source/gold/expert gate closes because these scripts pass.
