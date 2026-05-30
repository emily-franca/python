vetor = []
posicoes = []

for i in range(100):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

for i in range(len(vetor)):
    if vetor[i] == 30:
        posicoes.append(i)

if posicoes:
    print(f"O número 30 aparece nas posições: {posicoes} do vetor.")
else:
    print("O número 30 não foi encontrado no vetor.")
