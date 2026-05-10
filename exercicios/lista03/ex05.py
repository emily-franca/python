#Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética das alturas.

cont = 0
soma_altura = 0

while cont >= 0 and cont < 20:
    altura = float(input(f"Digite a altura da {cont+1}º pessoa: "))
    soma_altura = soma_altura + altura
    cont += 1
print(f"A média das alturas é: {soma_altura / 20:.2f}.")