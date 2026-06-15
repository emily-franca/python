frase = input("Digite a frase: ")





frase_normal = frase.replace(" ", "").lower()

print("-=" * 20)
if frase_normal == frase_normal[::-1]:
    print("Os caracteres digitados formam um Palíndromo! \n")
else:
    print("Os caracteres digitados NÃo formam um Palíndromo! \n")