#Construir um algoritmo que indique se o número digitado está entre 20 e 90 ou não.

num = int(input("Digite o número para validação: "))

if num >= 20 and num <= 90:
    print("O número está entre 20 e 90!")
else:
    print("O número NÃO está entre 20 e 90!")