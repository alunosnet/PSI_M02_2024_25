"""
Este programa vai utilizar um ciclo for para
calcular e mostrar a tabuada de um número
"""
numero = int(input("Qual o nº da tabuada:"))

"""
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
....
"""
for i in range(1,11):
    print(i," x ",numero," = ",i*numero)
