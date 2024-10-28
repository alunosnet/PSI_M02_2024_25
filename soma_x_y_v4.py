"""
Programa para somar todos os valores inteiros entre x e y
O utilizador é que indica os valores para x e para y
"""
x = int(input("Indique o primeiro valor a somar:"))
y = int(input("Indique o limite dos valores a somar:"))

soma = 0

if x < y:
    incremento = 1
else:
    incremento = -1

for i in range(x,y + incremento,incremento):
    soma = soma + i

print(soma)