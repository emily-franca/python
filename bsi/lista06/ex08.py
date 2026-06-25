def dia_caractere(num):
    if num < 1 or num > 7:
        return "*** ERRO: NÚMERO INVÁLIDO!"
    return dias[num - 1]

dias = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SAB"]

dia_num = int(input("Digite o número correspondente ao dia da semana (1-7): "))
print(f"Dia da semana: {dia_caractere(dia_num)}")