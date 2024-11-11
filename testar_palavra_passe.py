"""
1.testar se uma palavra passe é segura:
- tem de ter letras
- tem de ter pelo menos uma maiúscula e uma minuscula
- tem de ter números
- tem de ter pelo menos 8 carateres
- tem de ter um carater especial: !?@€.,;:-_
"""
A_M = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A_MIN = A_M.lower()
A_SIMBOLOS = "!@?,.;:_-+*\\"
A_NUMEROS="0123456789"
TEM_M   = False
TEM_MIN = False
TEM_S   = False
TEM_N   = False 
ppasse = input("Introduza a palavra passe a testar:")
#Testar maiusculas
for letra in A_M:
    if letra in ppasse:
        TEM_M = True
        break
        
#Testar minusculas
for letra in A_MIN:
    if letra in ppasse:
        TEM_MIN = True
        break
#Testar numeros
for letra in A_NUMEROS:
    if letra in ppasse:
        TEM_N = True
        break
#Testar simbolos
for letra in A_SIMBOLOS:
    if letra in ppasse:
        TEM_S = True
        break

if TEM_M == True and TEM_MIN==True and TEM_N==True and TEM_S==True and len(ppasse)>=8:
    print("Palavra passe segura")
else:
    print("Palavra passe não é segura")
    if TEM_MIN == False:
        print("Não tem minusculas")
    if TEM_M == False:
        print("Não tem maiusculas")