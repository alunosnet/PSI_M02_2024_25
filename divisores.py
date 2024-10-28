"""
Ler um número inteiro positivo do utilizador e mostrar todos os divisores desse número.
P.Ex.:
->6
6
3
2
1
->10
10
5
2
1
"""
numero = int(input("Qual o nº:"))
for divisor in range(numero,0,-1):
    if numero % divisor == 0:
        print(divisor)
