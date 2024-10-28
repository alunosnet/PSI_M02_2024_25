#programa para ler 10 números e indicar qual é o maior
pos_maior  = 1
maior = int(input("Nº"))
for i in range(9):
    n = int(input("Nº:"))
    if n > maior:
        maior = n
        pos_maior = i +2

print("O maior é ",maior, " e foi o ",pos_maior,"º a ser inserido.")