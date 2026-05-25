print("=" * 30)
print("PREÇO DO kWh POR TIPO")
print("-+" * 15)
preco_r = float(input("Preço kWh residencial (R$): "))
preco_c = float(input("Preço kWh comercial (R$): "))
preco_i = float(input("Preço kWh industrial (R$): "))

n = int(input("\nNúmero de consumidores: "))
total_kwh_r = 0
total_kwh_c = 0
total_kwh_i = 0

total_kwh_geral = 0
total_consumidores = 0

print("\n" + "-" * 30)
print("DADOS DOS CONSUMIDORES")
print("-" * 30)

for i in range(n):
    print(f"\nConsumidor {i + 1}:")
    id_consumidor = input("  Número de identificação: ")
    kwh = float(input("  Quantidade de kWh consumidos: "))
    tipo = input("  Tipo (R - residencial, C - comercial, I - industrial): ")
    
    if tipo == 'R' or tipo == 'r':
        total_pagar = kwh * preco_r
        total_kwh_r += kwh
    elif tipo == 'C' or tipo == 'c':
        total_pagar = kwh * preco_c
        total_kwh_c += kwh
    elif tipo == 'I' or tipo == 'i':
        total_pagar = kwh * preco_i
        total_kwh_i += kwh
    
    print(f"  → ID: {id_consumidor} - Total a pagar: R$ {total_pagar:.2f}")
    total_kwh_geral += kwh
    total_consumidores += 1
media_geral = total_kwh_geral / total_consumidores

print("\n" + "-+" * 15)
print("RESULTADOS")
print("=" * 40)
print(f"\nTotal kWh residencial: {total_kwh_r:.2f}")
print(f"Total kWh comercial: {total_kwh_c:.2f}")
print(f"Total kWh industrial: {total_kwh_i:.2f}")
print(f"\nMédia geral de consumo: {media_geral:.2f} kWh")