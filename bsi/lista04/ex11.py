vetor1 = []
for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    vetor1.append(num)

vetor2 = []
for i in range(10):
    if i % 2 == 0:  # índice par
        vetor2.append(vetor1[i] * 3)
    else:           # índice ímpar
        vetor2.append(vetor1[i] / 2)

print("\nVETOR 1:", end=" ")
for x in vetor1:
    print(f"{x:.2f}", end=" ")
print()

print("VETOR 2:", end=" ")
for x in vetor2:
    print(f"{x:.2f}", end=" ")
print()
