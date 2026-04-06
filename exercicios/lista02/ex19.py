'''Ler 2 valores (considere que não serão lidos valores iguais) e escrevê-los em ordem
crescente.'''
print("-----------ORDEM CRESCENTE-----------")
valor01 = int(input("Digite o primeiro valor: "))
valor02 = int(input("Digite o segundo valor: "))

if valor01 > valor02:
    maior = valor01
    menor = valor02
else:
    maior = valor02
    menor = valor01
print("---")
print(menor, maior)