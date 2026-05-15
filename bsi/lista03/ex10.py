#Construir um algoritmo que calcule o fatorial de um número N.
n = int(input("Digite um número: "))
res = 1

for i in range(1, n+1):
    res *= i
print(f"O fatorial do número {n} é: {res}")