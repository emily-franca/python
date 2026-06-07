A = []
for i in range(10):
    linha = []
    for j in range(10):
        valor = int(input(f"Digite o elemento da linha {i}, coluna {j}: "))
        linha.append(valor)
    A.append(linha)

print("\nMatriz A:")
for i in range(10):
    for j in range(10):
        print(f"{A[i][j]:3d}", end=" ")
    print()

soma = 0
for i in range(10):
    for j in range(i+1):
        soma += A[i][j]

print(f"\nSoma dos elementos abaixo da diagonal principal (incluindo a diagonal): {soma}")
