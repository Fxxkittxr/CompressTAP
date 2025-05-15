# compress_paloma_2_fixed.py
# Algoritmo de compressão baseado em dicionário de palavras
# Cada palavra única recebe um índice e o texto é substituído por esses índices
# Exemplo: "casa casa azul" -> "0 0 1", onde {0: "casa", 1: "azul"}

def compress_dict(text):
    words = text.split()
    dictionary = {}
    compressed = []
    index = 0
    for word in words:
        if word not in dictionary:
            dictionary[word] = str(index)
            index += 1
        compressed.append(dictionary[word])

    # salvar o dicionário e os dados comprimidos
    output = ' '.join(compressed) + "\nDICT:" + ';'.join(f"{v}:{k}" for k, v in dictionary.items())
    return output

with open("arquivo2.txt", "r", encoding="utf-8") as f:
    content = f.read()

compressed = compress_dict(content)

with open("arquivo2.txt.squeezed", "w", encoding="utf-8") as f:
    f.write(compressed)
