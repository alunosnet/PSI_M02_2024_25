#Pedir um nº inteiro ao utilizar e indicar se é par ou impar
# % calcula o resto da divisão inteira
# p.ex:  10 % 2 == 0 é par
#        11 % 2 == 0.5 é impar
numero = int(input("Introduza um nº:"))
resto = numero % 2
if resto ==0:
    print("É par")
else:
    print("É impar")

