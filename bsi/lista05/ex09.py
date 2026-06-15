# Verificar se o CPF é válido.

cpf = input("Informe o número do cpf (xxx.xxx.xxx-xx): ")
print("-=" * 20)

# Verificando o formato
if len(cpf) == 14 and cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
    numeros = cpf.replace(".", "").replace("-", "")

    if numeros.isdigit() and len(numeros) == 11:
        if numeros == numeros[0] * 11:
            print("CPF inválido! todos os dígitos são iguais. \n")
        else:
            soma1 = 0
            for i in range(9):
                soma1 += int(numeros[i]) * (10 - i)
            digito1 = (soma1 * 10) % 11
            if digito1 == 10:
                digito1 = 0

            soma2 = 0
            for i in range(10):
                soma2 += int(numeros[i]) * (11 - i)
            digito2 = (soma2 * 10) % 11
            if digito2 == 10:
                digito2 = 0

            # comparação dos dígitos
            if int(numeros[9]) == digito1 and int(numeros[10]) == digito2:
                print("CPF válido! \n")
            else:
                print("CPF inválido! \n")
    else:
        print("*** CPF inválido! Deve conter somente números. \n")
else:
    print("*** Formato inválido! Use xxx.xxx.xxx-xx \n")