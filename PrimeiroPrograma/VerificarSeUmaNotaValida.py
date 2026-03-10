"""
Exemplo:
Dado um valor que respresente uma nota entre 0 e 10, informar se a nota é válida.
Entrada: 5   Saída: Nota válida
Entrada: 52  Saída: Nota inválida
Entrada: -2  Saída: Nota inválida

"""

#ler a nota
nota = float (input("Digite uma nota: "))
# se a nota for maior do que 10
if nota > 10:
#   exibir nota inválida
    print("Nota Inválida")
#se estiver abaixo de 0
elif nota <0:
#   exibir nota inválida
    print("Nota Inválida")
#senão
else:
#exibir nota valida
    print ("Nota Válida")