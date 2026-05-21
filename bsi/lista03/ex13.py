#começa 1/n e termina n/1
soma = 0
valor = int(input("Valor da variável: "))

for i in range(1, valor+1):
    numerador = i
    denominador = valor - i + 1
    soma += numerador / denominador
print(f"O valor de S é: {soma:.2f}")

