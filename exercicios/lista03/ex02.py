#Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é par ou ímpar.

cont = 0

while cont >= 0 and cont < 15:
    num = int(input(f"Digite o {cont+1}º número para verificar: "))
    resto = num % 2
    if (resto != 0):
        print("Ímpar!")
    else:
        print("Par!")
    print("-" *5)
    cont += 1
