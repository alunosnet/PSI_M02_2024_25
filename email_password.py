#Programar para validar login (email e password)
email = input("Introduza o seu email:")
palavra_passe = input("Introduza a sua palavra passe:")

#testar se o emai é joaquim@gmail.com e palavra passe é 12345
if email == "joaquim@gmail.com" and palavra_passe=="12345":
    print("Acesso autorizado.")
else:
    print("Erro. Login falhou.")