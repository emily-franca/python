def maior_numero(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Valores iguais."

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

print(f"O maior número é: {maior_numero(a, b)}")