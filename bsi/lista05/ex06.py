meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

data = input(f"Data de nascimento (dd/mm/aaaa): ")
dia = data[:2]
mes = data[3:5]
ano = data[6::]

mes_extenso = meses[int(mes) -1]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")