#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que
#diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nasc
if idade >= 18:
    print(f"Você poderá votar esse ano!")
else:
    print(f"Você não poderá votar esse ano!")