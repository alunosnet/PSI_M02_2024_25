numero = float(input("Introduza um valor:"))
numero = numero + 0.5
soma = 0
mensagem = ""
for i in range(10):
    if i<9:
        mensagem = mensagem + str(numero) + ","
    else:
        mensagem = mensagem + str(numero)
    soma = soma + numero
    numero = numero + 0.5
print(mensagem,"=",soma)