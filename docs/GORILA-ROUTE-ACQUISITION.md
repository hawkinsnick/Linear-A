# GORILA linked-page acquisition

The [route registry](../research/gorila-route-acquisition.json) groups 755 attributed source-entry references into **367 distinct page URLs**. Of those, 607 entries share a URL with at least one other source entry. A page, source entry, inscription surface and physical object are distinct counting units.

On 2026-10-04 the collector completed and saved **135 linked page JPEGs**, covering routes attributed to 222 source entries. HTML and image SHA-256, byte lengths and image pixel sizes identify the acquired files. Pixel sizes are image dimensions, not object measurements. The public registry omits volatile image-session URLs; stable page URLs and exact file digests remain. Images stay private and are not republished.

Acquisition was interrupted by an execution network-policy denial of `https://cefael.efa.gr:443`. The remaining 232 routes have no completed acquisition record. This does not establish denial by CEFAEL, absence of the source image, or a scholarly access restriction. Some in-flight requests may have started; no completed record is asserted for them. Further acquisition awaits an allowed source route.

Automated downloads add **zero reading verifications**. The independently scoped ten-entry critical pilot records actual inspected target pages separately. Do not convert a downloaded page into a verified printed-page locator, an entry transcription, or certified object identity.

Run `python scripts/build_gorila_route_audit.py --check` offline. With authorized local assets, add `--verify-assets data/private/gorila-route-assets` to verify every saved HTML/JPEG hash and length. The optional acquisition script uses Pillow and limits requests to four workers with at most one request start per second; do not repeatedly refetch the collection in CI. Failed or incomplete acquisition never closes a reading or identity gate.
