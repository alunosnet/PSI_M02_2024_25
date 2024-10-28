"""
Mostrar os nº positivos inferiores a 100 com excepção dos que são multiplos de 3
"""

for i in range(1,100):
    if i % 3 != 0:
        print(i)