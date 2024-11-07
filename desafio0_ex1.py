"""
Um programa para ler 2 nº e indicar se são iguais ou diferentes.
Caso sejam diferentes indicar a diferença entre eles, com um valor positivo
"""

n1 = int(input("Nº:"))
n2 = int(input("Nº:"))

if n1==n2:
    print("Iguais")
else:
    print("Diferentes")
    diferenca = n1-n2
    if diferenca<0:
        diferenca = diferenca * (-1)
    print(diferenca)