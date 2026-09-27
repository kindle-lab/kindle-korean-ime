# KPM distribution

## Canonical repository manifest

Kindle clients should use only the unified kindle-lab KPM hub:

`https://raw.githubusercontent.com/kindle-lab/kpm-repo/main/manifest.json`

This source repository intentionally has **no root KPM repository manifest** and **no committed `.kpkg` artifact directory**.

## Package sources

The two KPM package source trees live under:

- `packaging/probe/` — read-only compatibility probe
- `packaging/korean-ime/` — Korean IME package

Each package source contains its own `manifest.json`. That file is embedded inside the resulting `.kpkg` and is distinct from the repository-level manifest maintained by `kindle-lab/kpm-repo`.

## Build and release flow

Normal pushes and pull requests:

1. run host tests;
2. cross-build the Kindle ARM binaries;
3. assemble both `.kpkg` files under `dist/`;
4. validate archive structure;
5. retain the binaries as GitHub Actions artifacts only.

A `v*` tag additionally publishes the built `.kpkg` files as GitHub Release assets. The tag must match the IME package version, for example `v0.6.5`.

The unified `kindle-lab/kpm-repo` repository remains the KPM-facing registry and keeps the currently verified package mirrors required by installed Kindle clients.
