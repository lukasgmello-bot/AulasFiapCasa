"""
Clausulas: Continue, Break e Else no laços
"""
cont = 0
while cont < 10:
    print("Comando 1")
    print("Comando 2")
    print("Comando 3")
    if cont == 5:
        cont = cont + 1
        break
        print("Comando 4")
        print("Comando 5")
        print("Comando 6")
        print("Comando 7")
        print("Comando 8")
    cont = cont + 1
else:
    print("O laço foi executado sem interrupção!")
