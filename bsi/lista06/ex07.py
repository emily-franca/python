def encontrar_mes(numero):
    if 1 <= numero <= 12:
        print(f"O mês correspondente ao número {numero} é {meses[numero - 1]}.")
    else:
        print("*** Número inválido. Digite um número entre 1 e 12.")

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

num_mes = int(input("Digite o número do mês (1-12): "))
encontrar_mes(num_mes)
