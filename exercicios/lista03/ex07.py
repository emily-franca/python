#Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a
#caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”.
#Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui.

tinta_disp = int(input("Informe a quantidade de tinta disponível (em %): "))

while tinta_disp > 2:
    print("Enquanto tem tinta a caneta escreve...")
    gasto = (tinta_disp * 2) / 100
    tinta_disp = tinta_disp - gasto
    print(f"Tinta restante: {tinta_disp:.2f}% \n")
print("-" *5)
print("Sem tinta!")
