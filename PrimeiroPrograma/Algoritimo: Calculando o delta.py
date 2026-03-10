"""
A terminologia: Entrada e Saida nos ajudam a:
- construir o agoritimo
- efetuar os testes com todos as possibilidades
- mostrar quantas entrada e saidas de dados teremos no algoritimo

Dados 3 valores pelo usuário que representa os valores de A, B e C, cacule o Delta.

ENTRADA: 1 2 3    SAÍDA: -8
ENTRADA: -1 2 3   SAÍDA: 16
Obs: ** significa exponenciação n²
"""
#ler o valor de a
a = int (input("Valor de a: "))

#ler o valor de b
b = int (input("Valor de b: "))

#ler o valor de c
c = int (input("Valor de c: "))

#calcular o delta
delta = b ** 2 - 4 * a * c
#exibir o delta
print(f"Delta: {delta:.1f}")