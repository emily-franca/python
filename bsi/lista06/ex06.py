def soma_intervalo(n1, n2):
    return sum(range(n1, n2 + 1))

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

print(f"A soma do intervalo entre {n1} e {n2} é: {soma_intervalo(n1, n2)}")