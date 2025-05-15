# uncompress_paloma_2_fixed.py
# Descomprime o arquivo baseado no índice e no dicionário de palavras

def decompress_dict(text):
    data, dict_part = text.split("\nDICT:")
    dictionary = {k: v for k, v in (item.split(":") for item in dict_part.split(";"))}
    words = data.strip().split()
    return ' '.join(dictionary[w] for w in words)

with open("arquivo2.txt.squeezed", "r", encoding="utf-8") as f:
    content = f.read()

decompressed = decompress_dict(content)

with open("arquivo2_restored.txt", "w", encoding="utf-8") as f:
    f.write(decompressed)
