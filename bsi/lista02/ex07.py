#Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o ano digitado é válido.
ano_nasc = int(input("Digite o ano de nascimento: "))

#considerando que a pessoa mais velha tem 130 anos
if ano_nasc >= 1896 and ano_nasc <= 2026:
    res = 2026 - ano_nasc
    print(f"A idade é: {res}")
else:
    print("Digite um ano válido.")