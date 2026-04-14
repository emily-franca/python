#Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.
valor01 = int(input("Digite o 1º valor: "))
valor02 = int(input("Digite o 2º valor: "))
valor03 = int(input("Digite o 3º valor: "))

if valor01 < valor02 and valor01 < valor03:
    menor = valor01
elif valor02 < valor01 and valor02 < valor03:
    menor = valor02
