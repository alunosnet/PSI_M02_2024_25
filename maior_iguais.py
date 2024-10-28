#Programa para dizer qual o maior de dois números ou se são iguais
n1 = int(input("Introduza um nº: "))
n2 = int(input("Introduza outro nº: "))

#testar se n1 é maior que o n2
if n1>n2:
    print(f"O  maior é {n1}")
else:
    if n2>n1:
        print("O maior é ",n2)
    else:
        print("São iguais")
