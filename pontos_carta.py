pontos = 12
infracao_leve=0
infracao_grave=0
infracao_mgrave=0
op = 0
while op !="4":
    #mostrar pontos
    print("Pontos:",pontos)
    if pontos==0:
        print("Perdeu a sua carta.")
    #mostrar as opções
    print("1.Muito Grave\n2.Grave\n3.Leve\n4.Terminar")
    #ler a opção
    op=input(":")
    #retirar os pontos
    if op=="1":
        pontos = pontos - 6
        infracao_mgrave = infracao_mgrave + 1
    if op=="2":
        pontos = pontos - 4
        infracao_grave = infracao_grave + 1
    if op=="3":
        if infracao_leve>0:
            pontos = pontos -1
        infracao_leve = infracao_leve + 1
    #se tem uma infracao m.grave e uma grave ou 2 graves perde os pontos todos
    if (infracao_mgrave==1 and infracao_grave==1) or (infracao_grave==2):
        pontos=0
    if pontos<0:
        pontos=0