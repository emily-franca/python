def verificar_divisivel(x, y):
    if y == 0:
        print("*** Não é possível dividir por zero!")
    elif x % y == 0:
        return 1
    else:
        return 0
num_x = int(input("Digite o número x: "))
num_y = int(input("Digite o número y: "))

if verificar_divisivel(num_x, num_y):
    print(f"{num_x} é divisível por {num_y}.")
else:
    print(f"{num_x} não é divisível por {num_y}.")
