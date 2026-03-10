"""
Dado um valor que represente uma nota entre 0 e 10, informar se a nota é valida.
Entrada: 5      Saída: Nota válida
Entrada: 32     Saída: Nota inválida
Entrada: -2     Saída: Nota inválida
"""

#aplicar operador lógico
nota1 = float(input("Digite a primeira nota: "))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Digite a segunda nota: "))
    if nota2 >= 0 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f"Média = {media:.1f}")
        if media >= 6:
            print("Aprovado")
        else:
            print("Reprovado")
    else:
        print("A segunda nota é invalida!")
else:
    print("A primeira nota é invalida!")