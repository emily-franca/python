print(".:: LEET SPEAK GENERATOR ::.\n")

leet_map = {
    "a": "4", "b": "8", "c": "<", "d": "|)", "e": "3",
    "f": "|=", "g": "9", "h": "|-|", "i": "1", "j": "_|",
    "k": "|<", "l": "1", "m": "|\\/|", "n": "|\\|", "o": "0",
    "p": "|>", "q": "0,", "r": "|2", "s": "5", "t": "7",
    "u": "(_)", "v": "\\/", "w": "\\/\\/", "x": "><", "y": "`/",
    "z": "2"
}

texto = input("Digite um texto: ")

resultado = ""
for letra in texto.lower():
    if letra in leet_map:
        resultado += leet_map[letra]
    else:
        resultado += letra

# Saída
print("\nTexto em leet:", resultado)
