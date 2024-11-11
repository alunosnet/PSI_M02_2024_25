"""
Programa para simular uma máquina de multibanco

"""

saldo = 0
escolha = None
while escolha != 4 or saldo <0:
    print("ATM\n1. Ver Saldo\n2.Depositar\n3.Levantar\n4.Terminar")
    escolha = int(input())
    if escolha == 1 and saldo >= 0:
        print(saldo)
    if escolha == 2:
        valor = float(input("Valor a depositar: "))
        #testar nº de casas decimais
        d = valor - round(valor,2)
        if d !=0:
            print("O valor não é válido, só pode ter 2 casas decimais.")
            continue
        if valor <= 0.01 or valor > 10000:
            print("O valor introduzido não é válido")
        else:
            saldo = saldo + valor
            print("O seu saldo atualmente é de ",saldo)
    if escolha == 3 and saldo >= 0:
        valor = float(input("Qual o valor a levantar: "))
        #testar nº de casas decimais
        d = valor - round(valor,2)
        if d !=0:
            print("O valor não é válido, só pode ter 2 casas decimais.")
            continue
        if valor < 10 or valor > 400: #or valor > saldo:
            print("Valor indicado não válido.")
        else:
            saldo = saldo - valor
            print("O seu saldo atualmente é de ",saldo)

