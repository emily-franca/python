print(".:: Número por Extenso ::.\n")

unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

num = int(input("Digite um número entre 0 e 99: "))

if 0 <= num <= 99:
    if num < 20:
        print(f"O número por extenso é: {unidades[num]}")
    else:
        dezena = num // 10
        unidade = num % 10
        if unidade == 0:
            print(f"O número por extenso é: {dezenas[dezena]}")
        else:
            print(f"O número por extenso é: {dezenas[dezena]} e {unidades[unidade]}")
else:
    print("Número inválido! Digite entre 0 e 99.")
