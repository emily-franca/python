def calcular_media(n1, n2):
    return (n1 + n2) / 2

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = calcular_media(n1, n2)
print(f"A média semestral é: {media:.2f}")

if media >= 6.0:
    print("PARABÉNS! Você foi aprovado!")