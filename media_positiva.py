#programa para ler três notas e indicar se a média é positiva ou negativa (>=10)
n1 = int(input("Primeira nota:"))
n2 = int(input("Segunda nota:"))
n3 = int(input("Terceira nota:"))

media = (n1 + n2 + n3)/3

if media>=10:
    print("Positiva")
else:
    print("Negativa")
