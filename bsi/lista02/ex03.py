#Calcule a soma de dois números, se o resultado for maior que 10, mostre-o na tela.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo valor: "))

res = num1 + num2

if res > 10:
    print(f"O resultado é: {res}")
else:
    print("Tente novamente!")
print("---")