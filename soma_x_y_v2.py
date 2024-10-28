"""
Programa para somar todos os valores inteiros entre x e y
O utilizador é que indica os valores para x e para y
"""
x = int(input("Indique o primeiro valor a somar:"))
y = int(input("Indique o limite dos valores a somar:"))

if x > y:
    #trocar os valores das variáveis
    t = x
    x = y
    y = t    

soma = 0
for i in range(x,y+1):
    soma = soma + i

print(soma)
