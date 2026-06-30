# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "Pillow==12.2.0"
# ]
# ///

import sys
import argparse
import shutil
import os
import subprocess
import platform
from pathlib import Path
from PIL import Image


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


def get_upscayl_model_path():
    if platform.system() == "Windows":
        return Path.home() / "Usr" / "Model" / "ncnn" / "models"
    else:
        return Path.home() / ".local" / "share" / "upscayl" / "models"


def upscale_image_if_needed(source_path, dest_path):
    try:
        with Image.open(source_path) as img:
            width, height = img.size

            if width < 800:
                print(
                    f"Image {source_path.name} width ({width}px) < 800px, upscaling..."
                )

                model_path = get_upscayl_model_path()
                upscayl_cmd = [
                    "upscayl-bin" if platform.system() == "Windows" else "upscayl",
                    "-m",
                    str(model_path),
                    "-n",
                    "4xLSDIR",
                    "-w",
                    "800",
                    "-i",
                    str(source_path),
                    "-o",
                    str(dest_path),
                ]

                result = subprocess.run(
                    upscayl_cmd, capture_output=True, text=True, encoding="utf-8"
                )

                if result.returncode != 0:
                    print(f"Error upscaling {source_path.name}: {result.stderr}")
                    shutil.copy(source_path, dest_path)
                    return False

                print(f"Upscaled {source_path.name} to {dest_path}")
                return True
            else:
                return False
    except Exception as e:
        print(f"Error checking image dimensions for {source_path}: {e}")
        return False


def get_image_source(content_dir):
    """Get image source directory from environment variable."""
    env_path = os.environ.get("MARK_IMAGES_SOURCE")
    if env_path:
        env_path = os.path.expandvars(env_path)
        path = Path(env_path)
        if path.exists():
            return path
    return None


_image_source_warned = False


def process_markdown(md_path, content_dir, output_dir, filename_suffix=""):
    if not md_path.exists():
        print(f"Error: Markdown file not found: {md_path}")
        sys.exit(1)

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    import re

    all_images = set()
    all_images.update(
        re.findall(
            r"!\[\]\(https://scillidan\.github\.io/cdn_image_post/(.+?)\.\w+\)",
            md_content,
        )
    )
    for match in re.findall(
        r"!\[([^\]]*)\]\(https://scillidan\.github\.io/cdn_image_post/(.+?)\.\w+\)",
        md_content,
    ):
        if isinstance(match, tuple):
            all_images.add(match[1])

    supported_formats = ["jpg", "jpeg", "png", "gif", "svg", "webp"]
    images_dir = content_dir / "_temp" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    if all_images:
        image_source = get_image_source(content_dir)

        if image_source:
            print(f"✓ Image source: {image_source}")
        else:
            env_path = os.environ.get("MARK_IMAGES_SOURCE")
            if env_path:
                env_path = os.path.expandvars(env_path)
                print(f"✗ Image source: {env_path} (not found)")
            else:
                print("✗ Image source: not configured")

            print("\nSet MARK_IMAGES_SOURCE in .env file or create symlink:")
            print("  assets\\images_a4 -> <your-images-directory>\n")
            sys.exit(1)

        missing_images = []
        found_count = 0

        for image_base_name in sorted(all_images):
            found_ext = None
            for ext in supported_formats:
                source_path = image_source / f"{image_base_name}.{ext}"
                if source_path.exists():
                    found_ext = ext
                    break

            if found_ext:
                source_filename = f"{image_base_name}.{found_ext}"
                source_path = image_source / source_filename
                dest_path = images_dir / source_filename

                if not dest_path.exists():
                    upscaled = upscale_image_if_needed(source_path, dest_path)
                    if not upscaled:
                        shutil.copy(source_path, dest_path)
                print(f"  ✓ {source_filename}")
                found_count += 1
            else:
                missing_images.append(image_base_name)
                print(f"  ✗ {image_base_name}.* (not found)")

        if missing_images:
            print(f"\n✗ Images: {found_count} found, {len(missing_images)} missing")
            sys.exit(1)
        else:
            print(f"✓ Images: all {found_count} found")
    else:
        image_source = None

    def replace_cdn_url(match):
        alt_text = match.group(1) if match.group(1) else ""
        image_name = match.group(2)

        for ext in supported_formats:
            test_path = images_dir / f"{image_name}.{ext}"
            if test_path.exists():
                return f"![{alt_text}](images/{image_name}.{ext})"

        return ""

    md_content_local = re.sub(
        r"!\[([^\]]*)\]\(https://scillidan\.github\.io/cdn_image_post/(.+?)\.\w+\)",
        replace_cdn_url,
        md_content,
    )

    import re as re2

    md_content_local = re2.sub(r"\n{3,}", "\n\n", md_content_local)

    suffix = f"-{filename_suffix}" if filename_suffix else ""
    md_processed_path = output_dir / f"{md_path.stem}{suffix}-processed.md"
    with open(md_processed_path, "w", encoding="utf-8") as f:
        f.write(md_content_local)

    return md_processed_path, images_dir


def copy_to_cmarker(images_dir):
    if not images_dir.exists():
        return
    try:
        cmarker_dir = (
            Path.home()
            / "AppData"
            / "Local"
            / "typst"
            / "packages"
            / "preview"
            / "cmarker"
            / "0.1.9"
        )
        if platform.system() != "Windows":
            cmarker_dir = (
                Path.home()
                / ".local"
                / "share"
                / "typst"
                / "packages"
                / "preview"
                / "cmarker"
                / "0.1.9"
            )

        cmarker_images_dir = cmarker_dir / "images"
        cmarker_images_dir.mkdir(parents=True, exist_ok=True)

        for image_path in images_dir.glob("*"):
            if image_path.suffix.lower() in [
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".svg",
                ".webp",
            ]:
                dest_path = cmarker_images_dir / image_path.name
                shutil.copy2(image_path, dest_path)

        print(f"Copied images to cmarker directory")
    except Exception as copy_error:
        print(f"Error copying images: {copy_error}")


def generate_typ_single(content_path, size_str, fonts, output_dir):
    md_processed_path, images_dir = process_markdown(
        content_path, content_path.parent, output_dir
    )
    copy_to_cmarker(images_dir)

    if not any(c.isalpha() for c in size_str):
        size_str = size_str + "pt"

    font_str = ", ".join(f'"{f}"' for f in fonts)
    content = f"""#import "@preview/cmarker:0.1.9"

#set page(paper: "a4", margin: 2%, columns: 2)
#set text(font: ({font_str}), size: {size_str})
#set par(justify: true)

#show raw.where(block: false): set text(font: ({font_str}), size: {size_str})
#show raw.where(block: true):  set text(font: ({font_str}), size: {size_str})

#show image: set align(center)
#set image(width: 100%)

#cmarker.render(read("../{md_processed_path.name}"))"""

    typ_path = output_dir / "typs" / f"{content_path.stem}.typ"
    typ_path.parent.mkdir(exist_ok=True)
    typ_path.write_text(content, encoding="utf-8")
    print(f"Created: {typ_path}")

    return typ_path, md_processed_path, images_dir


def generate_typ_dual_two_files(
    content_path_left, content_path_right, size_str, fonts, output_dir
):
    content_dir = content_path_left.parent

    md_left_processed, images_dir = process_markdown(
        content_path_left, content_dir, output_dir, "left"
    )
    md_right_processed, _ = process_markdown(
        content_path_right, content_dir, output_dir, "right"
    )
    copy_to_cmarker(images_dir)

    if not any(c.isalpha() for c in size_str):
        size_str = size_str + "pt"

    font_str = ", ".join(f'"{f}"' for f in fonts)
    output_name = f"{content_path_left.stem}-{content_path_right.stem}"
    content = f"""#import "@preview/cmarker:0.1.9"

#set page(paper: "a4", margin: 2%)
#set text(font: ({font_str}), size: {size_str})
#set par(justify: true)

#show image: set align(center)
#set image(width: 100%)

#grid(
  columns: (1fr, 1fr),
  gutter: 1em,
  [#cmarker.render(read("../{md_left_processed.name}"))],
  [#cmarker.render(read("../{md_right_processed.name}"))],
)"""

    typ_path = output_dir / "typs" / f"{output_name}.typ"
    typ_path.parent.mkdir(exist_ok=True)
    typ_path.write_text(content, encoding="utf-8")
    print(f"Created: {typ_path}")

    return typ_path, md_left_processed, md_right_processed, images_dir


def generate_output_stem(stem1, stem2):
    """Generate smart output stem for two-file comparison.

    Examples:
        article.md + article.zh-cn.md → article_zh-cn
        article.en.md + article.zh-cn.md → article_en_zh-cn
        file1.md + file2.md → file1-file2
    """
    if stem1 == stem2:
        return f"{stem1}-dual"

    if stem1 in stem2:
        idx = len(stem1)
        diff = stem2[idx:].lstrip("._-")
        if diff:
            return f"{stem1}_{diff}"
        return stem2
    elif stem2 in stem1:
        idx = len(stem2)
        diff = stem1[idx:].lstrip("._-")
        if diff:
            return f"{stem2}_{diff}"
        return stem1

    common_len = 0
    for c1, c2 in zip(stem1, stem2):
        if c1 == c2:
            common_len += 1
        else:
            break

    if common_len > 0:
        common = stem1[:common_len].rstrip("._-")
        diff1 = stem1[common_len:].lstrip("._-")
        diff2 = stem2[common_len:].lstrip("._-")

        if diff1 and diff2:
            return f"{common}_{diff1}_{diff2}"
        elif diff1:
            return f"{common}_{diff1}"
        elif diff2:
            return f"{common}_{diff2}"

    return f"{stem1}-{stem2}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate A4 Typst file from Markdown")
    parser.add_argument("path", help="Path to markdown file")
    parser.add_argument("--size", default="8pt", help="Font size (default: 8pt)")
    parser.add_argument("--font", dest="fonts", help="Font names (comma-separated)")
    parser.add_argument(
        "--two-column",
        dest="two_column",
        default=None,
        help="Two-column comparison with second file path",
    )
    args = parser.parse_args()

    check_dependencies()

    if args.fonts:
        fonts = [f.strip() for f in args.fonts.split(",")]
    else:
        fonts = ["MonaspiceNe NFM", "Sarasa Mono SC"]

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
    typs_dir = output_dir / "typs"
    typs_dir.mkdir(exist_ok=True)

    if args.two_column:
        content_path_right = Path(args.two_column)
        if not content_path_right.is_absolute():
            if content_path_right.parent == Path("."):
                content_path_right = content_dir / args.two_column
            else:
                content_path_right = Path.cwd() / args.two_column

        if not content_path_right.exists():
            print(f"Error: File not found: {content_path_right}")
            sys.exit(1)

        typ_path, md_left, md_right, images_dir = generate_typ_dual_two_files(
            content_path, content_path_right, args.size, fonts, output_dir
        )
        md_processed = [md_left, md_right]
        output_stem = generate_output_stem(content_path.stem, content_path_right.stem)
    else:
        typ_path, md_processed, images_dir = generate_typ_single(
            content_path, args.size, fonts, output_dir
        )
        output_stem = content_path.stem

    if isinstance(md_processed, list):
        for md in md_processed:
            print(f"Generated: {md}")
    else:
        print(f"Generated: {md_processed}")

    pdf_path = pdfs_dir / f"{output_stem}.pdf"
    result = subprocess.run(
        ["typst", "compile", "--root", str(project_root), str(typ_path), str(pdf_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"Typst compile error: {result.stderr}")
        sys.exit(1)
    print(f"Created: {pdf_path}")

    jpg_pattern = str(output_dir / f"{output_stem}_p%02d.jpg")
    result = subprocess.run(
        [
            "magick",
            "-density",
            "150",
            str(pdf_path),
            "-background",
            "white",
            "-alpha",
            "remove",
            "-quality",
            "90",
            jpg_pattern,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"ImageMagick error: {result.stderr}")
        sys.exit(1)
    print(f"Created: {output_dir}/{output_stem}_p*.jpg")

    if isinstance(md_processed, list):
        for md in md_processed:
            md.unlink()
    else:
        md_processed.unlink()

    try:
        cmarker_dir = (
            Path.home()
            / "AppData"
            / "Local"
            / "typst"
            / "packages"
            / "preview"
            / "cmarker"
            / "0.1.9"
        )
        if platform.system() != "Windows":
            cmarker_dir = (
                Path.home()
                / ".local"
                / "share"
                / "typst"
                / "packages"
                / "preview"
                / "cmarker"
                / "0.1.9"
            )

        cmarker_images_dir = cmarker_dir / "images"
        if cmarker_images_dir.exists():
            shutil.rmtree(cmarker_images_dir)
    except Exception as e:
        print(f"Warning: Could not cleanup cmarker images: {e}")

    if images_dir and images_dir.exists():
        shutil.rmtree(images_dir)
