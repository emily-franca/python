soma = 0
fatorial = 1
for i in range(20):
    if i > 0:
        fatorial = fatorial * i
    numerador = 100 - i
    denominador = fatorial

    soma += numerador / denominador
print(f"A soma dos 20 primeiros termos é aproximadamente: {soma:.3f}")