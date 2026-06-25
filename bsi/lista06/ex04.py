def pesoideal (altura, sexo):
    if sexo == "2":
        peso = (72.7 * altura) - 58
    elif sexo == "1":
        peso = (62.1 * altura) - 44.7
    else:
        return "Sexo inválido"
    
    return peso

altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo (1-Feminino ou 2-Masculino): ")

peso_ideal = pesoideal(altura, sexo)
print(f"O peso ideal é: {peso_ideal:.2f}")