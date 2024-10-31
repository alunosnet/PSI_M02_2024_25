numero = float(input("Introduza um valor:"))
numero = numero + 0.5
soma = 0
for i in range(10):
    if i<9:
        print(numero,end=",")
    else:
        print(numero,end="")
    soma = soma + numero
    numero = numero + 0.5
print("=",soma)