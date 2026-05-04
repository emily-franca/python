#Dado um conjunto de valores inteiros positivos, determinar qual o menor e qual o
# maior valor do conjunto. Um número com valor “0” (zero) indica o fim dos dados e
# não deve ser considerado.

num = 1
menor = 0
maior = 0
cont = 0

while num != 0:
    num = int(input("Digite um valor positivo: "))

    if(num < 0):
        print(f"Digite um número POSITIVO.")
    elif(num > 0):
        cont += 1
        if(cont == 1): #atribuindo os valores na primeira contagem
            maior = num
            menor = num
        else:
            if(num > maior): #verificação do maior valor
                    maior = num
            if(num < menor): #verificação do menor valor
                    menor = num
        print("Para sair digite '0' ")
    print("-" *3)
print("-" *5)
print(f"Maior: {maior}")
print(f"Menor: {menor}")