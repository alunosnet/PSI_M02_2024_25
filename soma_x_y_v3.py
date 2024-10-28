"""
Programa para somar todos os valores inteiros entre x e y
O utilizador é que indica os valores para x e para y
"""
x = int(input("Indique o primeiro valor a somar:"))
y = int(input("Indique o limite dos valores a somar:"))

soma = 0
if x < y:
    for i in range(x,y+1):
        soma = soma + i
else:
    for i in range(y,x+1):
        soma = soma + i

print(soma)