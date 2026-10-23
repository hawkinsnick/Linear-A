# Academic remediation: route rejection and case disposition

The retrieval layer now links every one of the 802 source documents to its current edition-target decision. The saved catalogue evidence establishes 220 target headings and rejects the original routes for HT 53a/b. Other routes remain unestablished. The two rejected URLs still appear in historical source records so the upstream assertion remains inspectable; they are not usable confirmed targets. No replacement is asserted. A bounded attempt to retrieve candidate viewer138 returned HTTP503 during this remediation; an offset alone is not a verified replacement.

```sh
python scripts/evidence_query.py --record 'HT 53a' --collection source-documents
python scripts/evidence_query.py --record 'HT 53a' --collection edition-route-decisions
```

Inspect `explicitly_linked_records` in the first result. `rejected_for_target` is true and `usable_confirmed_target_url` is null. The historical URL is preserved separately. A confirmed target heading is documentary source checking, not sign, reading or physical-object certification.

All fifteen legacy cases now link to explicit admission/disposition records. This uses the existing case-source-membership ledger, rather than pretending these memberships were newly discovered. U010 has two component pointers, not one combined inscription; U012/U013/U014 have no exact IDs in the pinned snapshot; U015 is interpretation-only. Their exclusion/routing is explicit. No legacy alternative pair is admitted. The scholarly attribution work in ACD-001 remains open.

```sh
python scripts/evidence_query.py --record U010 --collection legacy-cases
python scripts/evidence_query.py --record U015 --collection case-dispositions
python scripts/academic_remediation.py --check
python scripts/test_academic_remediation.py
```

The initial audit overstates the missing disposition of the five cases by omitting the existing membership ledger. The remediation makes those existing dispositions available in actual researcher queries. It closes ACD-002's scoped routing/exclusion criterion, not the underlying scholarly disagreements or snapshot coverage.

The frozen defect register and historical pilot scores remain unchanged. Read [current remediation status](../corpus-factory/academic-remediation-status.json) for item transitions and remaining open items. Source conflicts, inaccessible primary pages, actual expert decisions and independent evaluation still require their named evidence; no closure is inferred from tests passing.
