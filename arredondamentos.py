import math  #importar a biblioteca de funções math

x = 10.66

print(int(x))  #converte para inteiro sem arredondar
print(round(x,1)) #arredonda para o número par mais próximo

print(math.ceil(x)) #arredonda sempre para o inteiro seguinte (para cima)
print(math.floor(x)) #arredonda sempre para o inteiro anterior (para baixo)

#arredondar para cima se a parte decimal >= 0.5
parte_decimal = x - int(x)
if parte_decimal >= 0.5:
    x = int(x) + 1
else:
    x = int(x)
print(x)