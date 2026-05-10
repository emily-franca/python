#Escrever um algoritmo para ler dois valores e uma das seguintes operações a serem
# executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação
# e 4 – Divisão). Calcular e escrever o resultado dessa operação sobre os dois valores lidos.

print("--------------------.::MENU::.----------------------")
print("1 - ADIÇÃO\n 2 - SUBTRAÇÃO\n 3 - MULTIPLICAÇÃO\n 4 - DIVISÃO")
print("----------------------------------------------------")
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
op = int(input("Digite a operação que deseja realizar: "))

if op == 1:
    res = n1 + n2
elif op == 2:
    res = n1 - n2
elif op == 3:
    res = n1 * n2
elif op == 4:
    res = n1 / n2
else:
    print("Digite uma operação válida.")
print("----------------------------------------------------")
print(f"O resultado é: {res:.2f}")
