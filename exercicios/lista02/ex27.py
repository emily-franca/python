#Escreva um algoritmo que leia 4 valores (opção, a, b, c), onde opção é um valor
# inteiro e positivo e a, b, c são quaisquer valores reais. Escreva os valores lidos da seguinte maneira:
# se opção = 1 Þ escreva os 3 valores a, b, c em ordem crescente
# se opção = 2 Þ escreva os 3 valores a, b, c em ordem decrescente
# se opção = 3 Þ escreva os 3 valores de forma que o maior valor entre a, b, c fica entre os outros 2.
print("-------------------->>MENU<<---------------------")
print(" 1- Ordem CRESCENTE\n 2- Ordem DECRESCENTE\n 3- Maior valor fica entre os outros 2")
op = int(input("Digite a opção: "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
print("-------------------------------------------------")

if a > c and a > b: #a é maior
    maior = a
    if b > c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b
elif b > a and b > c:
    maior = b
    if a > c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a
elif c > a and c > b:
    maior = c
    if a > b:
        meio = a
        menor = b
    else:
        meio = b
        menor = a

if op == 1:
    print(f"{menor},{meio},{maior}")
elif op == 2:
    print(f"{maior},{meio},{menor}")
elif op == 3:
    print(f"{menor}, {maior}, {meio}")
else:
    print("Digite uma opção válida!")