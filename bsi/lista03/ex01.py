#Faça um algoritmo que:
#leia 20 números inteiros;
#escreva os números que são negativos;
#escreva a média dos números positivos.

cont = 1
negativos = ''
soma_positivos = 0
qtd_positivos = 0

while cont >= 1 and cont<= 20:
    num = int(input(f'Digite o {cont}º número:'))
    if(num < 0):
        negativos = negativos + str(num) + " "
    else:
        soma_positivos += num
        qtd_positivos += 1
    cont += 1
print('---')
print(f"Valores negativos: {negativos}")
print(f'A média dos valores positivos é: {soma_positivos/qtd_positivos:.2f}')