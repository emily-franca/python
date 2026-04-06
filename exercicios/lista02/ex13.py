'''Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do
vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.'''
print("====================================================")
print("                      TIME 01                       ")
print("----------------------------------------------------")
time01 = input("Nome do time: ")
gols01 = int(input("Quantidade de gols: "))
print("--------------------- TIME 02-----------------------")
time02 = input("Nome do time: ")
gols02 = int(input("Quantidade de gols: "))
print("---------------------RESULTADO----------------------")

if gols01 > gols02:
    print(f"{time01} foi o VENCEDOR!")
elif gols02 > gols01:
    print(f"{time02} foi o VENCEDOR!")
else:
    print("EMPATE!")