def perimetro(nmr_lados, medida_lado):
    return nmr_lados * medida_lado

def area(medida_lado):
    return medida_lado ** 2

nmr_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado (cm): "))

if nmr_lados == 3:
    print("O polígono é um TRIÂNGULO.")
    print(f"Perímetro: {perimetro(nmr_lados, medida_lado)} cm.\n")
elif nmr_lados == 4:
    print("O polígono é um QUADRADO.")
    print(f"Área: {area(medida_lado)} cm^2.\n")
elif nmr_lados == 5:
    print("O polígono é um PENTÁGONO.\n")
else:
    print("*** Polígono não identificado.\n")
