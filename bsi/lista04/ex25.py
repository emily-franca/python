MAT = []
for i in range(4):
    linha = []
    for j in range(5):
        valor = float(input(f"Digite o elemento da linha {i}, coluna {j}: "))
        linha.append(valor)
    MAT.append(linha)

SOMALINHA = []
for i in range(4):
    soma = sum(MAT[i])
    SOMALINHA.append(soma)

TOTAL = sum(SOMALINHA)

print("\nVetor SOMALINHA (soma de cada linha):")
for i in range(4):
    print(f"Linha {i}: {SOMALINHA[i]}")

print(f"\nTOTAL: {TOTAL}")
