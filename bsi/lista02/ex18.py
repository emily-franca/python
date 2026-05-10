#Ler 2 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valor01 = int(input("Digite o primeiro valor: "))
valor02 = int(input("Digite o segundo valor:"))

if valor01 > valor02:
    maior = valor01
else:
    maior = valor02
print(f"{maior} é o maior valor!")