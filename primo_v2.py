"""
Um programa que lê do utilizador um nº inteiro e
indica se o nº é primo.
Um nº é primo se só tiver como divisores o próprio nº e a unidade (1)
"""
numero = int(input("Insira o nº a testar:"))

for x in range(2,numero):
    if numero % x == 0:
        print("Não é primo")
        break
else:   #só é executado se o ciclo não for interrompido
    print("É primo")