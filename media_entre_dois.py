"""
Um programa para ler 20 números inteiros do utilizador e fazer a média dos números entre 20 e 50, inclusive [20,50]
"""
soma = 0
contar = 0
for i in range(20):
    n = int(input("Insira um nº:"))
    if n>=20 and n<=50:
        soma = soma + n
        contar = contar + 1

media = soma / contar

print("A média dos nº entre [20 e 50] foi de ",media)