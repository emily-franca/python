B = []
for i in range(4):
    linha = []
    for j in range(5):
        valor = float(input(f"Digite o elemento da linha {i}, coluna {j}: "))
        linha.append(valor)
    B.append(linha)

somas_linhas = []
for i in range(4):
    soma_linha = sum(B[i])
    somas_linhas.append(soma_linha)

soma_tot = sum(somas_linhas)

print("\nSoma de cada linha:")
for i in range(4):
    print(f"Linha {i}: {somas_linhas[i]}")

print(f"\nSoma de todos os elementos: {soma_tot}")
