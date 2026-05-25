n = int(input("Número total de reabastecimentos: "))

odometro_ini = float(input("Odômetro inicial (km): "))
odometro_ant = odometro_ini
total_km = 0
total_litros = 0

for i in range(n):
    odometro_atual = float(input(f"\nParada {i+1} - Odômetro (km): "))
    litros = float(input(f"Parada {i+1} - Combustível (litros): "))
    
    km_rodados = odometro_atual - odometro_ant
    
    if litros > 0:
        km_por_litro = km_rodados / litros
    else:
        km_por_litro = 0
    
    total_km += km_rodados
    total_litros += litros
    
    print(f"Km por litro: {km_por_litro:.2f} km/L")
    odometro_ant = odometro_atual
media_geral = total_km / total_litros

print("\n" + "-+" * 15)
print("RESULTADO")
print("-" * 30)
print(f"Quilometragem média: {media_geral:.2f} km/L")
print(f"Total km rodados: {total_km:.2f} km")
print(f"Total combustível: {total_litros:.2f} L")