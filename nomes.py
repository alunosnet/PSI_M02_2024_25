""""
Ler dois nomes e indicar qual dos dois é o maior (o que tem mais letras)
Alt gr
"""
nome1 = input("Introduza um nome:")
nome2 = input("Introduza outro nome:")
# t1 = len(nome1)
# t2 = len(nome2)
if len(nome1) > len(nome2):
    print(f"O maior nome é {nome1}")
elif len(nome2) > len(nome1):
    print(f"O maior nome é {nome2}")
else:
    print("Os dois nomes têm o mesmo tamanho")