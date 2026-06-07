A = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = float(input(f"Digite o elemento da linha {i}, coluna {j}: "))
        linha.append(valor)
    A.append(linha)

k = float(input("\nDigite a constante k: "))

for i in range(4):
    A[i][i] = A[i][i] * k

print("\nMatriz resultante:")
for i in range(4):
    for j in range(4):
        print(f"{A[i][j]:.2f}", end=" ")
    print()
