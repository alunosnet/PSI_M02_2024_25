"""
Um programa para calcular a duração total de um album. Para isso é necessário inserir a duração de cada música. A duração de cada música é inserida em segundos, mas a duração total deve ser mostrada em minutos:segundos.
Validar a duração da música. A duração não pode ser inferior ou igual 0 nem pode ser superior a 100 minutos.
a) Pedir quantas músicas primeiro Dinis, Afonso, Diogo
b) Ler até inserir duração 0 (zero) Dinis, Miguel, Francisco
c) Perguntar ao utilizador se deseja inserir mais músicas, Afonso x 2, Gabriel, Eduardo, João, Felipe 
"""
#versão b)
musica = 1
duracao_total = 0
#enquanto a duracao > 0
while musica != 0:
    #ler a duracao
    musica = int(input("Duração da música em segundos (0 para terminar):"))
    #validar os dados
    if musica < 0 or musica >= 6000:
        print("Duração não pode ser inferior 0 nem superior a 6000")
        continue
    #somar a duração ao total
    duracao_total = duracao_total + musica

#converter a duração total para minutos:segundos
minutos = duracao_total // 60
segundos = duracao_total % 60
#mostrar a duração total
print(f"A duração total do album é de {minutos}:{segundos}")