"""Programa para contar as vogais de uma frase"""
frase=input("Insira uma frase:")

contar = 0
for letra in frase:
    if letra in "aeiouAEIOU":
        contar = contar + 1
print("A frase indicada tem ",contar, " vogais")