"""
Programa para calcular a média das notas de 10 alunos e informar quantas notas são positivas
e quantas são negativas
"""
N_ALUNOS = 10

soma = 0
contar_positivas = 0
for _ in range(N_ALUNOS):
    nota = int(input("Introduza uma nota:"))
    soma = soma + nota
    #contar se a nota é positiva
    if nota>=10:
        contar_positivas = contar_positivas + 1

media = soma / N_ALUNOS
print(round(media,2))
print("Nº de positivas ",contar_positivas)
print("Nº de negativas",N_ALUNOS - contar_positivas)
#percentagem de positivas
p_positivas = contar_positivas / N_ALUNOS * 100
print("A percentagem de positivas foi de ",p_positivas)
print("A percentagem de negativas foi de ",100-p_positivas)
