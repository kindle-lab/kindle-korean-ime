#!/usr/bin/env python3
"""Offline structural validation for produced KPM package archives."""
import json
import sys
import tarfile

archives = sys.argv[1:]
if not archives:
    raise SystemExit("usage: validate_kpm.py ARCHIVE [ARCHIVE ...]")

for archive in archives:
    with tarfile.open(archive, "r:gz") as tar:
        names = {n.lstrip("./") for n in tar.getnames()}
        assert "manifest.json" in names, archive
        member = next(n for n in tar.getmembers() if n.name.lstrip("./") == "manifest.json")
        manifest = json.load(tar.extractfile(member))

        assert manifest["manifest_version"] == 2, archive
        assert manifest["id"] in {"korean-ime", "korean-ime-probe"}, archive
        assert len(manifest["version"]) == 3, archive
        assert set(manifest["supported_platforms"]) == {"kindlehf", "kindlepw2"}, archive
        assert "install.sh" in names and "uninstall.sh" in names, archive

print("KPM package archive validation: ok")
