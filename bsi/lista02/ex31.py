print("-------------------->>MENU<<---------------------")
print(" 0- Soma\n 1- Subtração\n 2- Mutiplicação\n 3- Divisão\n 4- Média")
op = int(input("Digite a opção: "))

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("-"*30)

if op == 0:
    res = n1 + n2
    print(f"Soma: {res}")
elif op == 1:
    res = n1 - n2
    print(f"Subtração: {res}")
elif op == 2:
    res = n1 * n2
    print(f"Multiplicação: {res}")
elif op == 3:
    if n2 != 0:
        res = n1 / n2
        print(f"Divisão: {res}")
    else:
        print("Erro: Não é possível dividir por zero.")
elif op == 4:
    res = (n1 + n2) / 2
    print(f"Média: {res}")
else:
    print("Digite uma opção válida.")