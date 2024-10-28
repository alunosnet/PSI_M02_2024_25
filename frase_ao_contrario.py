"""
Ler uma frase do utilizador e mostrar uma letra por linha
por ordem inversa
"""

frase = input("Introduza uma frase:")

#ciclo para percorrer a frase letra a letra mas por ordem invertida
for posicao in range(len(frase)-1,-1,-1):
    print(frase[posicao])
