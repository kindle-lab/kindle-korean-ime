# KPM packaging sources

This directory contains **source trees used to build KPM packages**, not a KPM repository.

- `probe/`: `korean-ime-probe`
- `korean-ime/`: `korean-ime`

Each child directory has its own package-level `manifest.json`, which is required inside the generated `.kpkg` archive.

The canonical repository-level manifest is maintained in `kindle-lab/kpm-repo`. Built `.kpkg` files belong in CI artifacts / GitHub Releases and are not committed here.
