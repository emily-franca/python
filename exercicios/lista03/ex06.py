#Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores são negativos.
num = 1
qtd_negativos = 0

while num != 0:
    num = int(input("Digite um valor: "))
    if(num < 0):
        qtd_negativos += 1
    print("Para sair digite '0'. \n")
print("-" *5)
print(f"Você digitou {qtd_negativos} números negativos.")