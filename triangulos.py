#ler os lados
a = float(input("Lado A:"))
b = float(input("Lado B:"))
c = float(input("Lado C:"))

#testar se é um triangulo
    #testar se os lados são positivos
    #testar se a soma de dois lados é sempre superior ao terceiro
if a <= 0 or  b <= 0 or c <= 0 or a+b < c or a+c<b or b+c<a:
    print("Triangulo não é válido")
else:
#classificar o triangulo
    #se todos iguais
    if a == b and b == c:
        print("Equilatero")  #TODO: continuar aqui 
    #se dois iguais
    #se não 
