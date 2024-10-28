#Funções para manipulação de strings
nome=" olá mundo "
marca='ford'
varias_linhas="""
Isto é uma string
com várias linhas
"""
#tamanho da string
print(len(nome))
#converter para maiusculas
print(marca.upper())
print(marca)
marca = marca.upper()
print(marca)
#converter para minusculas
marca = marca.lower()
print(marca)
#colocar a primeira letra em maiúsculas
marca = marca.capitalize()
print(marca)
#remove os espaço em branco no inicio e no final da string
print(len(nome))
nome=nome.strip()
print(len(nome))