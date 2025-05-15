# compress_paloma_1.py
# Algoritmo de compressão baseado em RLE (Run-Length Encoding)
# A ideia é substituir repetições consecutivas de caracteres por um número seguido do caractere
# Exemplo: "aaabbbbcc" -> "3a4b2c"

def compress_rle(text):
    compressed = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(f"{count}{text[i - 1]}")
            count = 1
    compressed.append(f"{count}{text[-1]}")  # último caractere
    return ''.join(compressed)

with open("arquivo1.txt", "r", encoding="utf-8") as f:
    content = f.read()

compressed = compress_rle(content)

with open("arquivo1.txt.squeezed", "w", encoding="utf-8") as f:
    f.write(compressed)
