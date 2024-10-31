"""
Calcular os dias que faltam para o final do mês com base na data indicada pelo utilizador
"""
#pedir a data
dia = int(input("Qual o dia:"))
mes = int(input("Qual o mês:"))
ano = int(input("Qual o ano:"))

dias_mes = 31

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_mes = 30
elif mes == 2:
    if (ano % 4 ==0 and ano % 100 !=0) or ano % 400==0:
        dias_mes = 29
    else:
        dias_mes = 28

faltam = dias_mes - dia
print("Faltam ",faltam," dias para o fim do mês")