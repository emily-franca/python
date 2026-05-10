#Ler um valor e escrever se é positivo, negativo ou zero.
num = float(input("Digite o valor para verificação: "))
if num > 0:
    print(f"O número digitado é positivo!")
elif num == 0:
    print(f"O número digitado é zero!")
else:
    print("O número digitado é negativo!")
print("---")