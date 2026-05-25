n = int(input("Quantos números quer testar? "))

for i in range(n):
    num = int(input(f"\n{i+1}º número: "))
    
    print(f"Divisores de {num}: ", end="") #end="" -> mantem na msm linha
    qtd = 0

    for divisor in range(1, num + 1):
        if num % divisor == 0:
            print(divisor, end=" ")
            qtd += 1
    
    print(f"\nqtd de divisores: {qtd}")