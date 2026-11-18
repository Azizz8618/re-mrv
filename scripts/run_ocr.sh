#!/bin/bash
# OCR всех страниц СПО_тексты.pdf: pdftoppm -r 200 -gray -png + tesseract rus+eng psm6
PDF="/home/azizz/Рабочий стол/Глиссада-6/СПО_тексты.pdf"
BASE="/tmp/.private/azizz/opencode/glissada"
mkdir -p "$BASE/ocr" "$BASE/img"

page_one() {
  local p="$1"
  local img="$BASE/img/p$(printf '%03d' "$p")"
  local out="$BASE/ocr/p$(printf '%03d' "$p")"
  if [ -s "$out.txt" ]; then return 0; fi
  pdftoppm -f "$p" -l "$p" -r 200 -gray -png -singlefile "$PDF" "$img" 2>/dev/null || return 1
  tesseract "$img.png" "$out" -l rus+eng --psm 6 2>/dev/null || return 1
  echo "$p"
}
export -f page_one
export PDF BASE

seq 1 335 | xargs -P 6 -I{} bash -c 'page_one "$@"' _ {} | sort -n > "$BASE/ocr/done.txt"
echo "DONE count=$(wc -l < "$BASE/ocr/done.txt")"
