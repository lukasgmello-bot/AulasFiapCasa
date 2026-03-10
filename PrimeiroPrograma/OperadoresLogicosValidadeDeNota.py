"""
Operadores Lógicos:
Não - not - negação
E   - and - conjunção
OU  - or  - disjunção

Email   Senha
OP1     OP2     E  OU
 V      V       V  V
 V      F       F  V
 F      V       F  V
 F      F       F  F

Exemplo:
Para op1 = True e op2 = False
1. op1 and op2
2. op1 or op2
3. op1 and not op2
4. not (op1 or op2)
5. not op1 and op2 or not op1 and op1

"""

op1 = True
op2 = False
print("5. ",not op1 and op2 or not op1 and op1)