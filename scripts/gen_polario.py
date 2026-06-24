# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import sys
import os
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


def escape_typst(text):
    return (
        text.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("#", "\\#")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("{", "\\{")
        .replace("}", "\\}")
    )


def get_image_source():
    env_path = os.environ.get("IMAGE_FAVORITE_IMAGES_SOURCE")
    if env_path:
        env_path = os.path.expandvars(env_path)
        if os.path.isdir(env_path):
            return Path(env_path)
    return None


def process_image(images_dir, image_name):
    image_source = get_image_source()

    if image_source:
        print(f"✓ Image source: {image_source}")
    else:
        env_path = os.environ.get("IMAGE_FAVORITE_IMAGES_SOURCE")
        if env_path:
            env_path = os.path.expandvars(env_path)
            print(f"✗ Image source: {env_path} (not found)")
        else:
            print("✗ Image source: not configured")

        print("\nSet IMAGE_FAVORITE_IMAGES_SOURCE in .env file or create symlink:")
        print("  favorite-image\\assets -> <your-images-directory>\n")
        sys.exit(1)

    supported_formats = ["jpg", "jpeg", "png", "gif", "svg", "webp"]
    image_base = Path(image_name).stem

    source_files = os.listdir(image_source)
    found_filename = None
    for ext in supported_formats:
        target = f"{image_base}.{ext}"
        if target in source_files:
            found_filename = target
            break

    if found_filename:
        source_path = Path(image_source) / found_filename
        dest_path = images_dir / found_filename

        if not dest_path.exists():
            shutil.copy2(str(source_path), str(dest_path))
        print(f"  ✓ {found_filename}")
    else:
        print(f"  ✗ {image_base}.* (not found)")
        sys.exit(1)

    return found_filename


def generate_typ(image_name, text_first, text_second, text_third, mode, start, resize, size, output_dir):
    typs_dir = output_dir / "typs"
    typs_dir.mkdir(exist_ok=True)

    flipped = mode == "landscape"
    text_first_escaped = escape_typst(text_first)
    text_second_escaped = escape_typst(text_second)
    text_third_escaped = escape_typst(text_third)
    image_rel_path = f"../../_temp/images/{image_name}"

    content = f'''#import "@preview/polario-frame:1.0.0": *

#let render-polario(params) = {{
  set page(fill: black, margin: 2%, flipped: params.flipped)
  set text(font: ("MonaspiceNe NFM", "Sarasa Mono SC"))
  let img = crop(bytes(read(params.img-path, encoding: none)), start: params.start, resize: params.resize)
  render(params.size, theme: params.theme, img: img, ext-info: params.ext-info)
}}

#let ext-info = (
  "background": rgb("#00000000"),
  "first": text(size: 11pt, fill: white)[
    {text_first_escaped}
  ],
  "second": text(size: 11pt, fill: white)[
    {text_second_escaped}
  ],
  "third": text(size: 11pt, fill: white)[
    _{text_third_escaped}_
  ],
)

#let params = (
  "ext-info": ext-info,
  "theme": "classic-bottom-three",
  "img-path": "{image_rel_path}",
  "flipped": {"true" if flipped else "false"},
  "start": {start},
  "resize": {resize},
  "size": {size},
)

#render-polario(params)
'''

    base_name = Path(image_name).stem
    typ_path = typs_dir / f"{base_name}.typ"
    typ_path.write_text(content, encoding="utf-8")
    print(f"Created: {typ_path}")
    return typ_path, base_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Polario frame from image")
    parser.add_argument("mode", choices=["landscape", "portrait"], help="Page orientation")
    parser.add_argument("image", help="Image filename")
    parser.add_argument("text_first", help="First text line (author)")
    parser.add_argument("text_second", help="Second text line (date)")
    parser.add_argument("text_third", help="Third text line (title)")
    parser.add_argument("start", help="Crop start, e.g. (5%%, 0%%)")
    parser.add_argument("resize", help="Resize ratio, e.g. 100%%")
    parser.add_argument("size", help="Frame size, e.g. (100%%, 100%%)")
    args = parser.parse_args()

    check_dependencies()

    project_root = Path(__file__).parent.parent.resolve()
    output_dir = project_root / "favorite-image" / "_output"
    output_dir.mkdir(exist_ok=True)

    images_dir = output_dir.parent / "_temp" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    pdfs_dir = output_dir / "pdfs"
    pdfs_dir.mkdir(exist_ok=True)

    image_name = process_image(images_dir, args.image)

    typ_path, base_name = generate_typ(
        image_name, args.text_first, args.text_second, args.text_third,
        args.mode, args.start, args.resize, args.size, output_dir
    )

    pdf_path = pdfs_dir / f"{base_name}.pdf"
    result = subprocess.run(
        ["typst", "compile", "--root", str(project_root), str(typ_path), str(pdf_path)],
        capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        print(f"Typst compile error: {result.stderr}")
        sys.exit(1)
    print(f"Created: {pdf_path}")

    jpg_path = output_dir / f"{base_name}.jpg"
    result = subprocess.run(
        ["magick", "-density", "150", str(pdf_path), "-background", "white",
         "-alpha", "remove", "-quality", "90", str(jpg_path)],
        capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        print(f"ImageMagick error: {result.stderr}")
        sys.exit(1)
    print(f"Created: {jpg_path}")
