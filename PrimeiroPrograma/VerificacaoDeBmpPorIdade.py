idade = float(input("Digite a sua idade:"))
bpm = int(input("Digite o valor do seus batimentos por minuto em repouso: "))
if idade >= 1 and idade <= 3:
    if bpm >= 98 and bpm <= 140:
        print("BPM dentro da média")
if idade >= 3 and idade <= 5:
    if bpm >= 80 and bpm <= 120:
        print("BPM dentro da média")
if idade >= 5 and idade <= 12:
    if bpm >= 75 and bpm <= 118:
        print("BPM dentro da média")
if idade >= 13:
    if bpm >= 60 and bpm <= 100:
        print("BPM dentro da média")
else:
    print("BPM fora da média, procure um médico ou especialista.")