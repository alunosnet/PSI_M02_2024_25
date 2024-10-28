idade = int(input("Idade:"))
if idade < 0 or idade > 120:
    print("Idade inválida")
elif idade >=0 and idade <= 11:
    print("Infância")
elif idade >=12 and idade <= 20:
    print("Adolescência")
elif idade >=21 and idade <= 75:
    print("Adulta")
else:
    print("Velhice")

