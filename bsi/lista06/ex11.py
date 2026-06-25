def converte_para_cm(pol):
    return pol * 2.54

polegada = float(input("Digite o valor em polegadas: "))
print(f"Equivale a: {converte_para_cm(polegada)} cm")