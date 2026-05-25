aud_canal4 = 0
aud_canal5 = 0
aud_canal9 = 0
aud_canal12 = 0
tot_espectadores = 0

num_casas = int(input("Digite o número de casas pesquisadas: "))

for i in range(num_casas):
    print(f"\nCasa {i+1}:")
    canal = int(input(" Canal (4, 5, 9, 12 ou 0):"))
    pessoas = int(input(" Número de espectadores: "))

    if canal == 4:
        aud_canal4 += pessoas
    elif canal == 5:
        aud_canal5 += pessoas
    elif canal == 9:
        aud_canal9 += pessoas
    elif canal == 12:
        aud_canal12 += pessoas

    tot_espectadores += pessoas
print("-"*6)
print("RESULTADO:")
if tot_espectadores == 0:
    print("Nenhuma pessoa assistindo TV.")
else:
    print(f"Canal 4: {aud_canal4 * 100 / tot_espectadores:.1f}%")
    print(f"Canal 5: {aud_canal5 * 100 / tot_espectadores:.1f}%")
    print(f"Canal 9: {aud_canal9 * 100 / tot_espectadores:.1f}%")
    print(f"Canal 12: {aud_canal12 * 100 / tot_espectadores:.1f}%")
    print(f"\nTotal de espectadores: {tot_espectadores}.")