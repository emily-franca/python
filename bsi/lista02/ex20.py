#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior
#deles.

valor01 = int(input("Digite o 1º valor: "))
valor02 = int(input("Digite o 2º valor: "))
valor03 = int(input("Digite o 3º valor: "))

if valor01 > valor02 and valor01 > valor03:
    maior = valor01
elif valor02 > valor03:
    maior = valor02
else:
    maior = valor03
print(f"O maior valor listado é: {maior}")