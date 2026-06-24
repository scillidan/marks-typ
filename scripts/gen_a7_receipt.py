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
import shutil
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


def generate_typ(content_path, size_str, font_str, scripts_dir, output_dir):
    typs_dir = output_dir / "typs"
    typs_dir.mkdir(exist_ok=True)

    if not content_path.exists():
        print(f"Error: Typst file not found: {content_path}")
        sys.exit(1)

    if not any(c.isalpha() for c in size_str):
        size_str = size_str + "pt"

    fonts = [f.strip() for f in font_str.split(",") if f.strip()]
    font_array = "(" + ", ".join(f'"{f}"' for f in fonts) + ",)"

    original_content = content_path.read_text(encoding="utf-8")
    
    template_rel = Path("../../../scripts/receipt-template.typ")
    template_rel_str = template_rel.as_posix()
    
    content = f"""#import "{template_rel_str}": *
#show: receipt-layout.with(size: {size_str}, font: {font_array})

{original_content}
"""
    generated_path = typs_dir / f"{content_path.stem}.typ"
    generated_path.write_text(content, encoding="utf-8")
    print(f"Created: {generated_path}")
    return generated_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate A7 receipt Typst file")
    parser.add_argument("path", help="Path to typst file")
    parser.add_argument("--size", default="8pt", help="Font size (default: 8pt)")
    parser.add_argument("--font", default="Sarasa Mono SC", help="Font(s), comma-separated")
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

    scripts_dir = Path(__file__).parent.resolve()

    typ_path = generate_typ(content_path, args.size, args.font, scripts_dir, output_dir)

    pdf_path = pdfs_dir / f"{content_path.stem}.pdf"
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
