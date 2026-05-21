x = float(input("Digite o valor de x: "))

soma_ex = 0.0
numerador = 1
fatorial = 1

for i in range(31):
    if i > 0:
        numerador *= x
        fatorial *= i
    fracao = numerador / fatorial
    soma_ex += fracao
print(f"O valor aproximado de e^{x} é: {soma_ex:.6f}")