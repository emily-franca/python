#Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se
#este número é par ou ímpar.

num = int(input("Digite o número: "))
res = num % 2

if res == 0:
    print("O número digitado é PAR!")
else:
    print("O número digitado é IMPAR!")