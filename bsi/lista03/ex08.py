#Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de
#inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva:
#• o número de inscrição e a altura do atleta mais alto;
#• o número de inscrição e a altura do atleta mais baixo;
#• a altura média do grupo de atletas.
qtd_atletas = 0
inscricao_alto = 0
altura_alto = 0
inscricao_baixo = 0
altura_baixo = 0
soma_alturas = 0

while inscricao != 0:
    inscricao = int(input("Número de inscrição: "))
    altura = float(input("Altura (cm): "))
    if qtd_atletas == 0: #tendo como base os primeiros valores digitados
        inscricao_alto = inscricao
        altura_alto = altura
        inscricao_baixo = inscricao
        altura_baixo = altura
    else:
        if(altura > altura_alto): #dados do atleta mais alto
            altura_alto = altura
            inscricao_alto = inscricao
        elif(altura < altura_baixo): #dados do atleta mais baixo
            altura_baixo = altura
            inscricao_baixo = inscricao
    print("Para sair digite '0'.")
