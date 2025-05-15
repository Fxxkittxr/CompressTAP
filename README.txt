Trabalho de Compressão - Paloma

Este projeto contém dois algoritmos de compressão e descompressão próprios, desenvolvidos para os arquivos "arquivo1.txt" e "arquivo2.txt".

1. compress_paloma_1.py / uncompress_paloma_1.py
   - Algoritmo: Run-Length Encoding (RLE)
   - Compacta repetições de caracteres consecutivos.
   - 100% reversível. Validação MD5 confirmada.

2. compress_paloma_2.py / uncompress_paloma_2.py
   - Algoritmo: Dicionário de Palavras
   - Substitui palavras por índices e armazena o dicionário no final do arquivo.
   - 100% reversível. Validação MD5 confirmada.

Arquivos incluídos:
- arquivo1.txt e arquivo2.txt (originais)
- arquivo1.txt.squeezed e arquivo2.txt.squeezed (compactados)
- arquivo1_restored.txt e arquivo2_restored.txt (descompactados)

Todos os arquivos descompactados foram validados usando MD5 e correspondem exatamente aos arquivos originais.

