A = []
for i in range(20):
    numero = float(input(f"Digite o {i}º número: "))
    A.append(numero)

# S = (A[0] - A[19])² + (A[1] - A[18])² + ... + (A[9] - A[10])²
S = 0
for i in range(10):
    diferenca = A[i] - A[19 - i]
    S += diferenca ** 2

print(f"\nValor de S: {S}")
