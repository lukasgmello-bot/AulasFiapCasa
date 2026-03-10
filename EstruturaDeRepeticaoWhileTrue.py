"""
Simulação do laço pré-condicional Repita.
Exemplo: Somar numeros até que seja digitado zero

"""

soma = 0
while True:
    n=float(input("Digite um numero: "))
    soma = soma + n
    if n == 0:
        break
    print("Somatória: ", soma)