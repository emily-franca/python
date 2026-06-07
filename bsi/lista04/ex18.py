A = []

for i in range(15):
    linha = []
    for j in range(25):
        valor = int(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
        linha.append(valor)
    A.append(linha)

print("\nRESULTADO:")
for i in range(15):
    for j in range(25):
        print(f"{A[i][j]}", end=" ")
    print()