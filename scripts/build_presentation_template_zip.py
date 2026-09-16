#!/usr/bin/env python3
"""Pre-render hook: package templates/presentation/ into a downloadable zip.

templates/presentation/ is excluded from the site build (it's a revealjs
source folder, not a knowledge-base page — see the `!templates/` entry in
_quarto.yml), so the zip built here is what software/presentation-template.qmd
links to. Runs on every `quarto render` / `quarto preview`, so the zip can't
drift out of sync with the template source, and it's not committed (see
.gitignore) — always regenerated fresh, like _site/ itself.
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "templates" / "presentation"
OUT = ROOT / "software" / "presentation-template-files" / "presentation-template.zip"

# Skip the template's own render output (present if someone ran `quarto
# render` inside templates/presentation/ while editing it) and OS cruft.
SKIP_NAMES = {".DS_Store", "template.html"}
SKIP_DIRS = {"template_files"}


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(SRC.rglob("*")):
            if path.is_dir():
                continue
            rel = path.relative_to(SRC)
            if path.name in SKIP_NAMES or SKIP_DIRS & set(rel.parts):
                continue
            zf.write(path, pathlib.Path("presentation-template") / rel)
    print(f"Built {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
