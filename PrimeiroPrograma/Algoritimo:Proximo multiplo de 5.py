"""
Dado um número pelo usuário, calcular e exibir o próximo multiplo de5.
Entrada: 13  Saída: 15
Entrada: 25  Saida: 30
"""

#Ler um numero dado pelo usuário
num = int(input("Digite um numero: "))
mult = int(input("Digite um valor multiplo: "))
#calcular o próximo multiplo de 5
prox_mult = num // mult * mult + mult

#exibir o próximo multiplo de 5
print(prox_mult)