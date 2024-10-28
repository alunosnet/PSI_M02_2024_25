""""
O utilizador está a fazer compras em um supermercado com um orçamento e uma capacidade de peso limitados. Seu objetivo é maximizar o número de itens que você pode comprar sem exceder seu orçamento e a capacidade de peso que você pode levar.
De cada vez que adicionar um produto à lista de compras deve indicar quanto dinheiro ainda sobra e quanto peso ainda pode carregar.
Quando o preço for 0 (zero) o programa termina.
"""

# ler o orçamento e o peso do utilizador
orcamento = float(input("Quanto dinheiro tem para as compras?"))
peso = float(input("Quanto peso pode carregar?"))

#enquanto tiver orçamento e peso
while orcamento > 0 and peso > 0:
    # ler o preço e o peso do produto comprado
    preco = float(input("Indique o preço do produto comprado:"))
    
    # se o preço é zero terminar o ciclo
    if preco == 0:
        break
    peso_produto = float(input("Indique o peso do produto comprado:"))
    # não posso ultrapassar o orçamento nem o peso
    if orcamento < preco or peso < peso_produto:
        print("Não tem dinheiro ou produto muito pesado")
    else:
        # atualizar o orçamento e o peso
        orcamento = orcamento - preco
        peso = peso - peso_produto
    # mostrar o orçamento e o peso restante
    print(f"Ainda tem {orcamento}€ e ainda pode carregar mais {peso}Kg") 

print("Acabou as suas compras")