m = int(input("Digite o número de linhas da matriz A: "))
n = int(input("Digite o número de colunas da matriz A (e linhas da matriz B): "))
p = int(input("Digite o número de colunas da matriz B: "))

A = []
print("\nDigite os elementos da matriz A:")
for i in range(m):
    linha = []
    for j in range(n):
        valor = float(input(f"A[{i}][{j}]: "))
        linha.append(valor)
    A.append(linha)

B = []
print("\nDigite os elementos da matriz B:")
for i in range(n):
    linha = []
    for j in range(p):
        valor = float(input(f"B[{i}][{j}]: "))
        linha.append(valor)
    B.append(linha)

C = []
for i in range(m):
    linha = []
    for j in range(p):
        soma = 0
        for k in range(n):
            soma += A[i][k] * B[k][j]
        linha.append(soma)
    C.append(linha)

print("\nMatriz A:")
for linha in A:
    print(linha)

print("\nMatriz B:")
for linha in B:
    print(linha)

print("\nMatriz C (Produto A x B):")
for linha in C:
    print(linha)
