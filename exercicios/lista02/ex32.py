v1 = int(input("Digite o primeiro valor inteiro: "))
v2 = int(input("Digite o segundo valor inteiro: "))

if v2 == 0:
    print(">> Erro: O segundo valor não pode ser zero!")
else:
    resto = v1 % v2
    print(f"Resto da divisão: {resto}")

    if resto == 1:
        resultado = (v1 + v2) + resto
        print(f"Resultado (Soma + Resto): {resultado}")
    elif resto == 2:
        if v1 % 2 == 0:
            status_v1 = "Par"
        else:
            status_v1 = "Ímpar"
            
        if v2 % 2 == 0:
            status_v2 = "Par"
        else:
            status_v2 = "Ímpar"   
        print(f"O primeiro valor ({v1}) é {status_v1} e o segundo valor ({v2}) é {status_v2}.")
    elif resto == 3:
        resultado = (v1 + v2) * v1
        print(f"Resultado (Soma * Primeiro): {resultado}")
    elif resto == 4:
        if v2 != 0:
            resultado = (v1 + v2) / v2
            print(f"Resultado (Soma / Segundo): {resultado}")
        else:
            print("Não foi possível dividir pela segunda variável pois ela é zero.")
    else:
        print(f"O quadrado de {v1} é {v1 ** 2}")
        print(f"O quadrado de {v2} é {v2 ** 2}")