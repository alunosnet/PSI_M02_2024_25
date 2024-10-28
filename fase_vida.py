idade = int(input("Idade:"))
if idade < 0 or idade > 120:
    print("Idade inválida")
if idade >=0 and idade <= 11:
    print("Infância")
if idade >=12 and idade <= 20:
    print("Adolescência")
if idade >=21 and idade <= 75:
    print("Adulta")
if idade >=76 and idade <= 120:
    print("Velhice")

