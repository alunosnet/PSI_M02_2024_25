#programa para ler 3 números e indicar qual é o maior
x1 = int(input("Indique um número: "))
x2 = int(input("Indique um número: "))
x3 = int(input("Indique um número: "))

if x1 > x2:
    maior = x1

if x2 > x1:
    maior = x2

if maior < x3:
    maior = x3

print(maior)