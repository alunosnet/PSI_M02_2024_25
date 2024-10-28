"""
Ler 10 letras, uma de cada vez e mostrar, no final, quantas
vogais foram introduzidas
"""
contar_vogais = 0
for _ in range(10):
    letra = input("Introduza uma letra:")
    letra = letra.strip() #remover os espaços em branco no  inicio e final da str
    if len(letra) != 1:
        print("Só pode inserir uma letra")
    else:
        if letra in "aeiouAEIOU":
            contar_vogais = contar_vogais + 1
print(contar_vogais)