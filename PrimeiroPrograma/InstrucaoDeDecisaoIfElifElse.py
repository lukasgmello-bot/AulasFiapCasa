"""
Sintaxe: Se Encadeado no python
Forma 1
if <condição1>:
    <bloco verdadeiro1>
else:
    if  <condição2>:
            <bloco verdadeiro2>
    else:
        <bloco outros>
Forma 2
if <condição1>:
    <bloco verdadeiro1>
elif <condição2>:
    <bloco verdadeiro2>
else:
    <bloco outros>

Exemplo:
Dado um número, verificar se ele "Positivi" ou "Nulo"
Entrada: 34  Saída: Positivo
Entrada: 0   Saída: Nulo
Entrada: -5  Saída: Negativo

"""

num = int (input("Digite um número: "))
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
        print("Nulo")