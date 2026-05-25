limite = 0.0005 #0,5 gramas -> 0,0005 Kg

massa_inicial = float(input("Massa inicial (Kg): "))
massa = massa_inicial
tempo = 0
ciclos = 0

while massa >= limite:
    massa = massa / 2
    tempo += 50
    ciclos += 1

print("-" * 30)
print(f"Massa inicial: {massa_inicial} Kg")
print(f"Massa final: {massa:.6f} Kg ({massa * 1000:.3f} gramas)")
print(f"Tempo necessário: {tempo} segundos ({ciclos} ciclos)")