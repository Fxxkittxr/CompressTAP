# uncompress_paloma_1.py
# Processo inverso da compressão RLE
# Lê pares de número + caractere e reconstrói a string original

import re

def decompress_rle(text):
    parts = re.findall(r'(\d+)(\D)', text)
    return ''.join(int(num) * char for num, char in parts)

with open("arquivo1.txt.squeezed", "r", encoding="utf-8") as f:
    content = f.read()

decompressed = decompress_rle(content)

with open("arquivo1_restored.txt", "w", encoding="utf-8") as f:
    f.write(decompressed)
