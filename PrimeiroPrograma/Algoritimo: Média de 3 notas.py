"""
# python é case sensitive ou seja, recebe apenas comando em minusculos

# Comando aprendidos

- Entrada de dados input ()
- Saída de dado - print()
- Processamento de dados: cálculos

Dados tres numero pelo usuário, calcular a média
Entrada: 10 12 20   Saída: 14 ""
"""

#ler o primeiro numero
nota1 = float(input("Digite a primeira nota: "))

#ler o segundo numero
nota2 = float(input("Digite a segunda nota: "))

#ler o terceiro numero
nota3 = float(input("Digite a terceira nota: "))

#calcular a média
media = (nota1 + nota2 + nota3) / 3

#exibir a média
# print("Á média das notas é: ",media) o que eu fiz
# aula: obs o .1f significa que eu quero que o numero saia com apenas uma casa decimal
print(f"Os valores {nota1}, {nota2} e {nota3} resultam a média = {media:.1f}")





