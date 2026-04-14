#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
valor01 = int(input("Digite o 1º valor: "))
valor02 = int(input("Digite o 2º valor: "))
valor03 = int(input("Digite o 3º valor: "))

if valor01 < valor02 and valor01 < valor03:
    soma = valor02 + valor03
elif valor02 < valor01 and valor02 < valor03:
    soma = valor01 + valor03
else:
    soma = valor01 + valor02
print(f"A soma dos dois maiores valores é: {soma}")