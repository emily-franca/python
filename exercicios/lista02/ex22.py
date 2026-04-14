#Ler 3 valores e escrevê-los em ordem crescente
valor01 = int(input("Digite o 1º valor: "))
valor02 = int(input("Digite o 2º valor: "))
valor03 = int(input("Digite o 3º valor: "))

#6,10,2

if valor01 > valor03 and valor01 > valor02: #valor01 é maior
    maior = valor01
    if valor02 > valor03:
        meio = valor02
        menor = valor03
    else:
        meio = valor03
        menor = valor02
elif valor02 > valor01 and valor02 > valor03:
    maior = valor02
    if valor01 > valor03:
        meio = valor01
        menor = valor03
    else:
        meio = valor03
        menor = valor01
elif valor03 > valor01 and valor03 > valor02:
    maior = valor03
    if valor01 > valor02:
        meio = valor01
        menor = valor02
    else:
        meio = valor02
        menor = valor01
else:
    print("Inválido!")
print(f"{menor}, {meio}, {maior}.")