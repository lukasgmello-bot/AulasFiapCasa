"""
Um caixa eletronico dispensa cédulas de 10, 20, 50 e 100 reais.
Dado um valor pelo usuario (considere que ja seja multiplo de 10), exibir a quantidade de cédulas que
devem ser dispensadas para compor este valor.
Entrada de: 190    Saída: R$100,00 - 1 cédula(s)
                          R$50,00 - 1 cédula(s)
                          R$20,00 - 2 cédula(s)
                          R$10,00 - 0 cédula(s)

Entrada de: 80     Saída: R$100,00 - 0 cédula(s)
                          R$50,00 - 1 cédula(s)
                          R$20,00 - 1 cédula(s)
                          R$10,00 - 1 cédula(s)

"""

# Ler a quantia
quantia = int(input("Digite a quantia: R$ "))

# calcular a quantia de cedulas de 100
ced100 = quantia // 100 #1
# Atualizar a quantia
quantia = quantia % 100 #90

# calcular a quantia de cedulas de 50
ced50 = quantia // 50 #1
# Atualizar a quantia
quantia = quantia % 50 #40

# calcular a quantia de cedulas de 20
ced20 = quantia // 20 #2
# Atualizar a quantia
quantia = quantia % 20 #0

# calcular a quantia de cedulas de 10
ced10 = quantia // 10 #0
# Atualizar a quantia
quantia = quantia % 10

print(f"R$ 100.00 = {ced100}\n"
      f"R$ 50.00 = {ced50}\n"
      f"R$ 20.00 = {ced20}\n"
      f"R$ 10.00 = {ced10}")