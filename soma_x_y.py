"""
Programa para somar todos os valores inteiros entre x e y
O utilizador é que indica os valores para x e para y
"""
x = int(input("Indique o primeiro valor a somar:"))
y = int(input("Indique o limite dos valores a somar:"))

if x > y:
    print("Os valores não são válidos. O primeiro deve ser inferior ao segundo.")
else:
    soma = 0
    for i in range(x,y):
        soma = soma + i

    print(soma)