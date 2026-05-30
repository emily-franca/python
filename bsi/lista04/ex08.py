vetor1 = []
print("-" * 10, "Vetor 01", "-" * 10)
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor1.append(numero)

vetor2 = []
print("-" * 10, "Vetor 02", "-" * 10)
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor2.append(numero)

vetor3 = []
for i in range(5):
    soma = vetor1[i] + vetor2[i]
    vetor3.append(soma)

print("-+" * 20)
print("VETOR 1:", end=" ")
for x in vetor1:
    print(f"{x:.2f}", end=" ")
print()  #quebra de linha para o vetor 2

print("VETOR 2:", end=" ")
for x in vetor2:
    print(f"{x:.2f}", end=" ")
print()

print("VETOR 3:", end=" ")
for x in vetor3:
    print(f"{x:.2f}", end=" ")
print()
