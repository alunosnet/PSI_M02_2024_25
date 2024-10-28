"""
O Sr. Joaquim tem um restaurante com 10 mesas. Cada mesa tem 5 lugares.
Faça um programa que leia as entradas para cada mesa, partindo do principio de que cada vez que os clientes entram ocupam uma mesa, mas podem ocupar mais do 5 lugares.
Não deve permitir a entrada de mais clientes para mesas/lugares do que os disponíveis.

Ex.
5
Mesas ocupadas: 1
Lugares disponíveis: 45
10
Mesas ocupadas: 2
Lugares disponiveis: 35
35
Mesas ocupadas: 3
Lugares disponiveis: 0
Programa termina

Ex.
1
Mesas ocupadas: 1
Lugares disponíveis: 49
1
Mesas ocupadas: 2
Lugares disponíveis: 48
1
Lugares disponíveis: 47
Mesas ocupadas: 3
1
Mesas ocupadas: 4
Lugares disponíveis: 46
1
Mesas ocupadas: 5
Lugares disponíveis: 45
...
10
...
Programa termina

"""

mesas = 10
lugares = mesas * 5

for mesas_ocupadas in range(mesas):
    nr_clientes = int(input("Quantas pessoas para entrar: "))
    if nr_clientes>lugares:
        print("Não tem lugares para tantos clientes")
        break
    #ocupar 1 mesa
    mesas = mesas - 1
    #ocupar os lugares
    lugares = lugares - nr_clientes
    print("Mesas ocupadas: ",mesas_ocupadas+1)
    print("Lugares disponíveis: ",lugares)

print("O restaurante está cheio")