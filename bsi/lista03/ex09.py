#Faça um algoritmo que calcule e imprima os valores de y, onde
#y = (3+2x+(6x)**2) / (1+9x+(16x)**2) -> x var 1 até 5
i = 1

while i <= 5: 
    res = (3 + 2*i + (6*i)**2) / (1 + 9*i + (16*i)**2)
    print(f"Para x = {i:.4f}")
    print(f"resultado é aproximadamente: {res:.4f} \n")
    i += 0.1


