numero = int(input("Introduza um nº: "))
soma = 0
for i in range(1,numero):
    resto = numero % i
    if resto == 0:
        soma = soma + i

if soma == numero:
    print("Nº é perfeito")
else:
    print("Nº não é perfeito. A soma dos seus divisores foi ",soma)
