'''Escrever um algoritmo para ler a quantidade de horas aula dadas por dois professores
e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem
salário total maior.'''

print("=========================================================")
print("                      PROFESSOR 01                       ")
print("---------------------------------------------------------")
horas_1 = float(input("Quantidade de horas aula: "))
valor_hora1 = float(input("Valor recebido por hora: "))
print("---------------------------------------------------------")
print("                      PROFESSOR 02                       ")
print("---------------------------------------------------------")
horas_2 = float(input("Quantidade de horas aula: "))
valor_hora2 = float(input("Valor recebido por hora: "))
print("---------------------------------------------------------")

prof01 = horas_1 * valor_hora1
prof02 = horas_2 * valor_hora2

if prof01 > prof02:
    print("PROFESSOR 01 tem o maior salário total!")
else:
    print("PROFESSOR 02 tem o maior salário total!")