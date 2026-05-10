#Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10,
#caso contrário escrever NÃO É MAIOR QUE 10!
num = float(input("Digite o valor a ser verificado: "))
if num > 10:
    print("É maior que 10!")
elif num < 10:
    print("Não é maior que 10!")
else:
    print("O valor digitado é igual 10!")