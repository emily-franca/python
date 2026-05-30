A = []

for i in range(3):
    numero = float(input(f"Digite o {i+1}º número: "))
    A.append(numero)

print(f"O somatório dos valores do vetor A é: {sum(A)}")
