"""
Um programa para calcular o somatório de dois números.
P.Ex. Somatório 2 a 15: 2+3+4+5+6+7+8+9+10+11+12+13+14+15
"""
primeiro = int(input("Insira o primeiro nº do somatório:"))
ultimo = int(input("Insira o último nº do somatório:"))

soma = 0
for i in range(primeiro,ultimo+1):
    soma = soma + i
print("O somatório de ",primeiro," a ",ultimo, " é ",soma)