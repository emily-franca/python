def calc_hipotenusa(a, b):
    return (a**2 + b**2) ** 0.5

cateto_a = float(input("Valor do cateto a: "))
cateto_b = float(input("Valor do cateto b: "))

hipotenusa = calc_hipotenusa(cateto_a, cateto_b)

print(f"A hipotenusa é: {hipotenusa:.2f}")