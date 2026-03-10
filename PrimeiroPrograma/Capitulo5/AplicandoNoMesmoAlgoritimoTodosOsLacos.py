"""
Resolvendo um problema com todos os laços
Exemplo: Dados 10 médios pelo usuário, contar quantos foram aprovados e quando foram reprevados

"""

aprovados = 0
reprovados = 0
voltas = 1

while voltas <= 10:
    media = float(input("Digite a média: "))
    if media >= 6:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
    voltas = voltas + 1

print(f"Aprovados: {aprovados}\nReprovados: {reprovados}")