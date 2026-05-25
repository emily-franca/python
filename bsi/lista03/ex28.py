pontos_d = 0  
pontos_e = 0  
jogada = ""

print("-+" * 15)
print("PARTIDA DE PINGUE-PONGUE")
print("-" * 30)
print("Informe D (direito) ou E (esquerdo)")
print("Para encerrar, digite fim\n")

while True:
    jogada = input("Jogada: ")
    
    if jogada == "fim":
        break
    
    if jogada == "D" or jogada == "d":
        pontos_d += 1
    elif jogada == "E" or jogada == "e":
        pontos_e += 1
    
    print(f"  Plac({pontos_d} x {pontos_e})")
    
    if (pontos_d >= 21 or pontos_e >= 21) and abs(pontos_d - pontos_e) >= 2: #abs - valor absoluto
        break
    
    if pontos_d > 21 or pontos_e > 21:
        if abs(pontos_d - pontos_e) == 2:
            break
print("\n" + "-" * 30)
print("RESULTADO")
print("-" * 30)

if pontos_d > pontos_e:
    print(f"Vencedor: Jogador DIREITO ({pontos_d} x {pontos_e})")
else:
    print(f"Vencedor: Jogador ESQUERDO ({pontos_e} x {pontos_d})")