# == Default options
# size: 8(pt)
# font: MonaspiceNe NFM, Sarasa Mono SC
# Image source: Set MARK_IMAGES_SOURCE in .env file

set dotenv-load

# == A4 single file (2-column layout)
a4 path size="" font="":
    uv run scripts/gen_a4.py "{{path}}" \
        {{ if size != "" { "--size " + size } else { "" } }} \
        {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}

# == A4 two-column comparison (file1 left, file2 right)
a4-two-column path1 path2 size="" font="":
    uv run scripts/gen_a4.py "{{path1}}" --two-column "{{path2}}" \
        {{ if size != "" { "--size " + size } else { "" } }} \
        {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}

# == A6 (mark)
a6 path size="" font="":
    uv run scripts/gen_a6.py "{{path}}" \
        {{ if size != "" { "--size " + size } else { "" } }} \
        {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}

# == A7 receipt
a7-receipt path size="" font="":
    uv run scripts/gen_a7_receipt.py "{{path}}" \
        {{ if size != "" { "--size " + size } else { "" } }} \
        {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}

# == Polario frame (favorite-image)
gen_polario mode image text-first text-second text-third start resize size:
    uv run scripts/gen_polario.py {{mode}} "{{image}}" "{{text-first}}" "{{text-second}}" "{{text-third}}" "{{start}}" "{{resize}}" "{{size}}"

# == Clean generated files from a content directory
clean dir:
    @python -c "import shutil; from pathlib import Path; \
        d = Path('{{dir}}'); \
        [shutil.rmtree(p, ignore_errors=True) for p in [d / '_output', d / '_temp'] if p.exists()]; \
        print(f'Cleaned: {d}')"

# == Clean all generated files
clean-all:
    @python -c "import shutil; from pathlib import Path; \
        dirs = ['mark', 'post', 'post_laws-of-software-engineering', 'post_chat', 'receipt', 'favorite-image']; \
        [shutil.rmtree(p, ignore_errors=True) for d in dirs for p in [Path(d) / '_output', Path(d) / '_temp'] if p.exists()]; \
        print('Cleaned all')"