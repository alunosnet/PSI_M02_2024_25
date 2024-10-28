#programa para ler 10 números e indicar qual é o maior
pos_maior  = 1
for i in range(10):
    n = int(input("Nº:"))
    #se é o primeiro nº
    if i == 0:
        maior = n
    else:
        if n > maior:
            maior = n
            pos_maior = i +1

print("O maior é ",maior, " e foi o ",pos_maior,"º a ser inserido.")