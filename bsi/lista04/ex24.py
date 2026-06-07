A = []
print("Digite os elementos da matriz A (3x5):")
for i in range(3):
    linha = []
    for j in range(5):
        valor = float(input(f"A[{i}][{j}]: "))
        linha.append(valor)
    A.append(linha)

B = []
print("\nDigite os elementos da matriz B (3x5):")
for i in range(3):
    linha = []
    for j in range(5):
        valor = float(input(f"B[{i}][{j}]: "))
        linha.append(valor)
    B.append(linha)

SOMA = []
for i in range(3):
    linha = []
    for j in range(5):
        linha.append(A[i][j] + B[i][j])
    SOMA.append(linha)

print("\nMatriz SOMA (A + B):")
for i in range(3):
    for j in range(5):
        print(f"{SOMA[i][j]:.2f}", end=" ")
    print()
