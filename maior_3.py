#programa para ler 3 números e indicar qual é o maior
x1 = int(input("Indique um número: "))
x2 = int(input("Indique um número: "))
x3 = int(input("Indique um número: "))

#verificar se o x1 é o maior
if x1 > x2:
    if x1 > x3:
        print(f"O maior é o {x1}")

#verificar se o x2 é o maior
if x2 > x1:
    if x2 > x3:
        print(f"O maior é {x2}")

#verificar se o x3 é o maior
if x3 > x1:
    if x3 > x2:
        print(f"O maior é {x3}")

