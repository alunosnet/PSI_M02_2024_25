#pedir a quantidade comprada
quantidade = int(input("Introduza a quantidade comprada:"))

p_desconto = 0
if quantidade >= 500 and quantidade<=1000:
    p_desconto = 5/100
elif quantidade > 1000:
    p_desconto = 8/100

#calcular o preco
preco = 1000 * quantidade

#calcular o valor do desconto
valor_desconto = preco * p_desconto

#calcular  o preço final
preco_final = preco - valor_desconto

print(f"A percentagem de desconto foi de {p_desconto} que correspondente ao valor de {valor_desconto} e o preço final foi de {preco_final}")
