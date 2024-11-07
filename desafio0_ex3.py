"""
Programa para ler as notas de uma turma e indicar o nº do aluno com melhor nota.
Deve começar por ler o nº de alunos
"""

melhor_nota = -1
numero_aluno = -1

nr_alunos = int(input("Quantos alunos tem a turma? "))
for i in range(nr_alunos):
    nota = int(input(f"Nota do aluno nº {i+1}: "))
    if i==0:
        melhor_nota = nota
        numero_aluno = 1
    if nota > melhor_nota:
        melhor_nota = nota
        numero_aluno = i + 1

print("O aluno com melhor nota é o nº ",numero_aluno)