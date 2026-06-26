# == Default options
# size: 8(pt)
# font: MonaspiceNe NFM, Sarasa Mono SC
# Image source: Set MARK_IMAGES_SOURCE in .env file

set dotenv-load

# == post (A4, 2-column)
a4 path size="" font="":
    uv run scripts/gen_a4.py "{{path}}" \
        {{ if size != "" { "--size " + size } else { "" } }} \
        {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}

# == post (A4, 2-column) (file1 left, file2 right)
a42 path1 path2 size="" font="":
    uv run scripts/gen_a4.py "{{path1}}" --two-column "{{path2}}" \
        {{ if size != "" { "--size " + size } else { "" } }} \
        {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}

# == mark (A6)
a6 path size="" font="":
    uv run scripts/gen_a6.py "{{path}}" \
        {{ if size != "" { "--size " + size } else { "" } }} \
        {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}


# == receipt (A7)
receipt path size="" font="":
    uv run scripts/gen_a7_receipt.py "{{path}}" \
        {{ if size != "" { "--size " + size } else { "" } }} \
        {{ if font != "" { "--font \"" + font + "\"" } else { "" } }}

# == favorite-image (polario frame)
polario mode image text-first text-second text-third start resize size:
    uv run scripts/gen_polario.py {{mode}} "{{image}}" "{{text-first}}" "{{text-second}}" "{{text-third}}" "{{start}}" "{{resize}}" "{{size}}"