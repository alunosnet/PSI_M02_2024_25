#Sequência de Collatz
numero = int(input("Valor inicial: "))

while numero!=1:
    #calcular o resto da divisão por 2
    resto = numero % 2
    if resto == 0:
        numero = numero // 2
    else:
        numero = numero * 3 + 1
    print(numero)
    