"""
Um programa para calcular a duração total de um album. Para isso é necessário inserir a duração de cada música. A duração de cada música é inserida em segundos, mas a duração total deve ser mostrada em minutos:segundos.
Validar a duração da música. A duração não pode ser inferior ou igual 0 nem pode ser superior a 100 minutos.
a) Pedir quantas músicas primeiro Dinis, Afonso, Diogo
b) Ler até inserir duração 0 (zero) Dinis, Miguel, Francisco
c) Perguntar ao utilizador se deseja inserir mais músicas, Afonso x 2, Gabriel, Eduardo, João, Felipe 
"""
#versão a)

#pedir o nº de músicas
nr_musicas = int(input("Quantas músicas deseja inserir?"))
duracao_total = 0
#ciclo para o nº de músicas
for i in range(nr_musicas):
    #ler a duração de uma música
    musica = int(input(f"Duração da música {i+1} em segundos:"))
    #validação
    while musica <= 0 or musica>=6000:
        print("A duração da música não é válida")
        musica = int(input(f"Duração da música {i+1} em segundos:"))
    #somar a duração ao total
    duracao_total = duracao_total + musica

#converter a duração total para minutos:segundos
minutos = duracao_total // 60
segundos = duracao_total % 60
#mostrar a duração total
print(f"A duração total do album é de {minutos}:{segundos}")

#versão b)

#enquanto a duracao > 0
    #ler a duracao
    #validar os dados
    #somar a duração ao total

#converter a duração total para minutos:segundos
#mostrar a duração total

#versão c)

#enquanto deseja inserir mais
    #ler a duração
    #validar
    #somar
    #perguntar se deseja continuar a inserir

#converter
#mostrar