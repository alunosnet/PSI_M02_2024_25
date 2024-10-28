#programa que indica se uma pessoa é adulto em função do ano de nascimento
ano_nascimento = int(input("Indique o ano em que nasceu:"))

idade = 2024 - ano_nascimento

if idade >= 18:
    print("És adulto")
    print("Já podes votar e tirar a carta")
else:
    print("Ainda não és adulto")
    print("Não podes votar")
    
print("Fim do programa")