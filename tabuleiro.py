"""
Desenhar um tabuleiro de xadrez utilizando *, espaço em branco
"""

for linhas in range(8):
    if linhas % 2 == 0:
        for colunas in range(4):
            print(" *",end="")
    else:
        for colunas in range(4):
            print("* ",end="")
    print("")