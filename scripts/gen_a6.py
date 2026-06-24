# /// script
# requires-python = ">=3.12"
# ///

# Requirements:
# - typst: https://typst.app/
# - ImageMagick: https://imagemagick.org/ (command: magick)
# - uv: https://docs.astral.sh/uv/

import sys
import argparse
import subprocess
from pathlib import Path


def check_dependencies():
    missing = []
    if not shutil.which("typst"):
        missing.append("typst")
    if not shutil.which("magick"):
        missing.append("ImageMagick (magick)")

    if missing:
        print("Error: Missing required dependencies:")
        for dep in missing:
            print(f"  - {dep}")
        print("\nInstall instructions:")
        print("  typst:        https://typst.app/")
        print("  ImageMagick:  https://imagemagick.org/")
        sys.exit(1)


import shutil


def generate_typ(content_path, size_str, font_str, output_dir):
    typs_dir = output_dir / "typs"
    typs_dir.mkdir(exist_ok=True)

    if not content_path.exists():
        print(f"Error: Markdown file not found: {content_path}")
        sys.exit(1)

    if not any(c.isalpha() for c in size_str):
        size_str = size_str + "pt"

    fonts = [f.strip() for f in font_str.split(",") if f.strip()]
    font_array = "(" + ", ".join(f'"{f}"' for f in fonts) + ",)"

    md_rel_path = f"../../{content_path.name}"

    content = f"""#import "@preview/cmarker:0.1.8"

#set page(paper: "a6", margin: 5%)
#set text(font: {font_array}, size: {size_str})
#set par(justify: true)

#cmarker.render(read("{md_rel_path}"))"""

    typ_path = typs_dir / f"{content_path.stem}.typ"
    typ_path.write_text(content, encoding="utf-8")
    print(f"Created: {typ_path}")
    return typ_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate A6 Typst file from Markdown")
    parser.add_argument("path", help="Path to markdown file")
    parser.add_argument("--size", default="8pt", help="Font size (default: 8pt)")
    parser.add_argument("--font", default="MonaspiceNe NFM, Sarasa Mono SC", help="Font(s), comma-separated")
    args = parser.parse_args()

    check_dependencies()

    content_path = Path(args.path)
    if not content_path.is_absolute():
        content_path = Path.cwd() / content_path

    if not content_path.exists():
        print(f"Error: File not found: {content_path}")
        sys.exit(1)

    content_dir = content_path.parent
    project_root = content_dir.parent
    output_dir = content_dir / "_output"
    output_dir.mkdir(exist_ok=True)

    pdfs_dir = output_dir / "pdfs"
    pdfs_dir.mkdir(exist_ok=True)

    typ_path = generate_typ(content_path, args.size, args.font, output_dir)

    pdf_path = output_dir / "pdfs" / f"{content_path.stem}.pdf"
    result = subprocess.run(
        ["typst", "compile", "--root", str(project_root), str(typ_path), str(pdf_path)],
        capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        print(f"Typst compile error: {result.stderr}")
        sys.exit(1)
    print(f"Created: {pdf_path}")

    jpg_pattern = str(output_dir / f"{content_path.stem}_p%02d.jpg")
    result = subprocess.run(
        ["magick", "-density", "150", str(pdf_path), "-background", "white",
         "-alpha", "remove", "-quality", "90", jpg_pattern],
        capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        print(f"ImageMagick error: {result.stderr}")
        sys.exit(1)
    print(f"Created: {output_dir}/{content_path.stem}_p*.jpg")
