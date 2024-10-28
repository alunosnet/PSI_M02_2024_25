#programa para simular uma calculadora simples
#deve solicitar dois números e a operação a realizar ao utilizador
#e mostrar o resultado
escolha = "s"
while escolha == "s":
    op = input("Qual a operação a realizar (+ ou s, - ou sub, * ou m, / ou d,somatório):")
    v1 = float(input("Introduza um nº:"))
    v2 = float(input("Introduza outro nº:"))
    #remover os espaços em branco
    op = op.strip()
    #operações
    if op.lower() in "+s":
        resultado = v1 + v2
    elif op.lower() in "-sub":
        resultado = v1 - v2
    elif op.lower() in "*m":
        resultado = v1 * v2
    elif op.lower() in "/d":
        resultado = v1 / v2
    elif op.lower() == "somatório":
        i1 = int(v1)
        i2 = int(v2)
        if i1 > i2:
            print("O primeiro valor tem de ser inferior ao segundo")
            continue
        resultado = 0
        for i in range(i1,i2):
            resultado = resultado + i
    else:
        print("Operação não é válida")
        #definir a variável resultado com nada
        resultado = None

    if resultado is not None:
        print(resultado)
    #perguntar se pretende continuar
    escolha = input("Pretende continuar a fazer contas (s/n)? ")
    escolha = escolha.strip().lower()