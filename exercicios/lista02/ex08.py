#Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de
#idade ou acima de 65 anos.
idade = int(input("Digite a idade: "))
if idade >= 18 and idade <= 65:
    print("Maior de idade!")
elif idade > 65:
    print("Acima de 65 anos.")
else:
    print("Menor de idade!")
