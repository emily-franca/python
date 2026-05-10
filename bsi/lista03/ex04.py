#Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos números ímpares entre 1 e 100.

cont = 1
soma_par = 0
soma_impar = 0

while cont >= 1 and cont <= 100:
    resto = cont % 2
    if(resto != 0):
        soma_impar = soma_impar + cont
    else:
        soma_par = soma_par + cont
    cont += 1
print(f"A soma dos números pares é: {soma_par}")
print(f"A soma dos números ímpares é: {soma_impar}")