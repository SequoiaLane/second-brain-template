#!/usr/bin/env python3
"""Build the Cowork upload files from cowork/plugin/.

Writes to cowork/dist/:
    second-brain-plugin.zip   upload under Customize > Plugins
    capture-skill.zip         fallback: upload under Customize > Skills
    recall-skill.zip          fallback: upload under Customize > Skills

Run after editing anything in cowork/plugin/.
"""

import zipfile
from pathlib import Path

here = Path(__file__).resolve().parent
plugin = here / "plugin"
dist = here / "dist"
dist.mkdir(exist_ok=True)


def zip_dir(src: Path, dest: Path, root_name: str) -> None:
    # Fixed timestamps keep the zips byte-identical across rebuilds.
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(src.rglob("*")):
            if f.is_file() and f.name != ".DS_Store":
                arc = Path(root_name) / f.relative_to(src)
                info = zipfile.ZipInfo(str(arc), date_time=(2026, 1, 1, 0, 0, 0))
                info.external_attr = 0o644 << 16
                z.writestr(info, f.read_bytes(), zipfile.ZIP_DEFLATED)
    print(f"wrote {dest.relative_to(here.parent)}")


zip_dir(plugin, dist / "second-brain-plugin.zip", "second-brain")
for skill in ("capture", "recall"):
    zip_dir(plugin / "skills" / skill, dist / f"{skill}-skill.zip", skill)
