#Programa para simular um registo num site
email = input("introduza o email:")
palavra_passe = input("Introduza a palavra passe:")
palavra_passe_repetida = input("introduza a palavra passe novamente:")

#testar se as palavras passe são diferentes
if palavra_passe != palavra_passe_repetida:
    print("As palavras passe não são iguais.")
else:
    print("Registo efetuado com sucesso.")