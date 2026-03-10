"""
Laço contador para - for.
Exemplo: Exibir a tubuada de um numero dado pelo usuário

"""

tab= int(input("Digite a tabuada: "))
for volta in range(1, 11, 1):
    mult = tab * volta
    print(f"{tab} x {volta} = {mult}")