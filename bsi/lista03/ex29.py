limite_kg = float(input("Limite diário (kg): "))
limite_g = limite_kg * 1000
peso_total = 0
resposta = 's'

print("-+" * 15)
while resposta == 's' or resposta == 'S':
    peso_peixe = float(input("Peso do peixe (g): "))
    
    peso_total += peso_peixe
    
    if peso_total > limite_g:
        print("-" * 40)
        print("LIMITE EXCEDIDO!")
        print(f"Peso total: {peso_total}g ({peso_total/1000:.2f}kg)")
        break
    print(f"Peso total: {peso_total}g ({peso_total/1000:.2f}kg)")
    resposta = input("Informar peso de mais um peixe: s (SIM) / n (NAO)? ")