# Kindle Korean IME

KPM-installable Korean keyboard / IME for jailbroken Kindle devices.

Korean installation guide: [docs/BLOG-KO-INSTALL.md](docs/BLOG-KO-INSTALL.md)

## Status

**Development / guarded device-validation stage.**

Current package versions:

- Korean IME: **0.6.5**
- Compatibility Probe: **0.2.5**

The Dubeolsik composition core, host tests, and ARM bridge builds are implemented. Device-specific behavior still requires real-Kindle validation, so this repository should not be treated as a universal compatibility claim.

## Repository roles

This repository is the **source repository**. It owns code, tests, packaging inputs, CI, and release provenance.

The canonical KPM installation manifest is maintained separately at:

`https://raw.githubusercontent.com/kindle-lab/kpm-repo/main/manifest.json`

Built `.kpkg` files are not committed to this source repository. Normal CI runs keep them as GitHub Actions artifacts; tagged releases publish them as GitHub Release assets. The KPM hub mirrors the currently verified packages needed by Kindle clients.

Current source release target: **v0.6.5**. Release assets are produced from CI; Kindle installation continues to use the canonical KPM hub above.

## Layout

```text
src/                    C sources
tests/                  host-side tests
packaging/
  probe/                 KPM package source for the read-only probe
  korean-ime/            KPM package source for the IME
scripts/                 validation helpers
docs/                    installation and safety notes
.github/workflows/       CI / release workflow
```

Each directory under `packaging/` contains its own `manifest.json` because KPM requires a package manifest inside the `.kpkg` archive. Those are **package manifests**, not repository manifests. The only canonical **repository manifest** for installation lives in `kindle-lab/kpm-repo`.

## Goal

- Install, update and uninstall through KPM
- Native Kindle keyboard integration
- Dubeolsik Korean layout
- Hangul composition including compound vowels/finals
- Correct composition-aware Backspace
- English/Korean switching through the native keyboard language control
- Clean rollback on uninstall

## Development plan

1. Compatibility probe
2. Device-specific ARM builds and native keyboard integration
3. KPM-distributed Korean Keyboard package
4. Native preedit/commit/replace integration where supported

## Safety

Do not install an experimental IME binary on a Kindle until its model/firmware has passed the compatibility probe. The probe itself is designed not to modify rootfs or keyboard configuration.

## Credits

The project design references the MIT-licensed Kingul project by hy1o and current KindleModding/KPM conventions. New composition/backspace logic and packaging are being developed separately for this project.
