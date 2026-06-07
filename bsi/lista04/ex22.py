A = []
for i in range(20):
    linha = []
    for j in range(20):
        valor = float(input(f"Digite o elemento da linha {i}, coluna {j}: "))
        linha.append(valor)
    A.append(linha)

for i in range(20):
    divisor = A[i][i] 
    for j in range(20):
        A[i][j] = A[i][j] / divisor

print("\nRESULTADO:")
for i in range(20):
    for j in range(20):
        print(f"{A[i][j]:.2f}", end=" ")
    print()
