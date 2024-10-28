idade = int(input("Idade:"))
if idade < 0 or idade > 120:
    print("Idade inválida")
else:
    if idade >=0 and idade <= 11:
        print("Infância")
    else:
        if idade >=12 and idade <= 20:
            print("Adolescência")
        else:
            if idade >=21 and idade <= 75:
                print("Adulta")
            else:
                print("Velhice")

