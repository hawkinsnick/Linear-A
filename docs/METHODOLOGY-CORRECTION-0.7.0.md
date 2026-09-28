# 0.7.0 methodology correction

During 0.7.0 auditing, the `site_id` field inherited from 0.6.0 was confirmed
to have been generated from the document-label prefix rather than decoded from
SigLA's explicit find-place field.

0.7.0 renames it `site_group_heuristic`, does not call it canonical site
metadata, and treats cross-group portability as descriptive sensitivity only.
A future release should populate canonical site IDs by joining the decoded
source-explicit find-place value through a reviewed mapping table.
