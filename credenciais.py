"""
Programa para testar as credenciais (email e password)
Permitir três tentativas
"""
tentativas = 3

while tentativas>0:
    print(f"Tem {tentativas} tentativas")
    email = input("Email: ")
    password = input("Password: ")
    #se login correto
    if email == "joaquim@gmail.com" and password=="12345":
        print("Login com sucesso")
        break
    #login falhou
    tentativas = tentativas - 1
    if email != "joaquim@gmail.com" and password != "12345":
        print("Login falhou")
    elif email != "joaquim@gmail.com":
        print("Email inválido")
    else:
        print("Password errada!")
    if tentativas == 0:
        print("Esgotou as 3 tentativas de login, tente novamente mais tarde!")