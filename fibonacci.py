"""
2. Série de Fibonacci até N: Escreva um programa que imprime a série de Fibonacci até um número N fornecido pelo usuário. Lembre-se de que a série de Fibonacci é uma sequência onde cada número é a soma dos dois anteriores, começando com 0 e 1.
"""
x1 = 0
x2 = 1
n = int(input("Quantos nº da sequência pretende?"))
print(x1)
print(x2)
for i in range(n-2):
    soma = x1 + x2
    print(soma)
    x1 = x2
    x2 = soma