B = []
for i in range(10):
    linha = []
    for j in range(20):
        valor = float(input(f"Digite o elemento da linha {i}, coluna {j}: "))
        linha.append(valor)
    B.append(linha)

soma_quinta_linha = sum(B[4])

print(f"\nSoma dos elementos da quinta linha: {soma_quinta_linha}")