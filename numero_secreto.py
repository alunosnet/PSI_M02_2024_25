#sortear um número entre 1 e 10
import random

#sortear o nº
numero_secreto = random.randint(1,10)
print(numero_secreto)

#pedir ao utilizador o nº
t1 = int(input("Introduza um nº (1 a 10):"))

#testar e informar se é maior, igual ou menor
if numero_secreto == t1:
    print("Acertou!")
else:
    if t1 > numero_secreto:
        print("O nº secreto é menor")
    else:
        print("O nº secreto é maior")
############################################################
    #pedir ao utilizador o nº segunda vez
    t1 = int(input("Introduza um nº (1 a 10):"))

    #testar e informar se é maior, igual ou menor
    if numero_secreto == t1:
        print("Acertou!")
    else:
        if t1 > numero_secreto:
            print("O nº secreto é menor")
        else:
            print("O nº secreto é maior")
        ############################################################
        #pedir ao utilizador o nº terceira vez
        t1 = int(input("Introduza um nº (1 a 10):"))

        #testar e informar se é maior, igual ou menor
        if numero_secreto == t1:
            print("Acertou!")
        else:
            print("O nº secreto era ",numero_secreto)
