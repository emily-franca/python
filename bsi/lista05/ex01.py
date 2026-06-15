frase01 = input("String 1: ")
frase02 = input("String 2: ")

print(f"Tamanho de '{frase01}': {len(frase01)} caracteres.")
print(f"Tamanho de '{frase02}': {len(frase02)} caracteres.")

if len(frase01) == len(frase02):
    print("As duas strings possuem o mesmo tamanho!")
else:
    print("As duas strings são de tamanhos diferentes!")


if frase01 == frase02:
    print("As duas strings possuem o mesmo conteúdo!")
else:
    print("As duas strings possuem conteúdos diferentes!")