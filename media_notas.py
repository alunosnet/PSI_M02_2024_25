"""
Programa para calcular a média das notas de 10 alunos
"""
N_ALUNOS = 10

soma = 0
for _ in range(N_ALUNOS):
    nota = int(input("Introduza uma nota:"))
    soma = soma + nota

media = soma / N_ALUNOS
print(round(media,2))