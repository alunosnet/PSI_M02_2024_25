"""
Um programa que lê do utilizador a hora e 
indica a parte do dia
"""
hora = int(input("Hora:"))

if hora>=5 and hora<=7:
    print("Madrugada")
elif hora>=8 and hora<=12:
    print("Manhã")
elif hora>=13 and hora<=19:
    print("Tarde")
else:
    print("Noite")
