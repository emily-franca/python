A = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    A.append(numero)

S = 0
for i in range(5):
    if A[i] != 0: #não dividir por zero
        S += i / A[i]

print(f"\nValor de S: {S:.2f}")

cont = 0
for i in range(5):
    if i < A[i]:
        cont += 1

print(f"Quantidade de termos com numerador menor que denominador: {cont}")
