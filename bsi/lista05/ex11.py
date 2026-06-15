import random

print(".:: JOGO DA FORCA ::. \n")
opcoes = ["programacao", "estudar", "python", "livro"]

palavra = random.choice(opcoes)
palavra_oculta = ["_"] * len(palavra)

erros = 0
max_erros = 6

print(f"A palavra é: {' '.join(palavra_oculta)}")

while erros < max_erros and "_" in palavra_oculta:
    letra = input("Digite uma letra: \n").lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_oculta[i] = letra
        print(f"A palavra é: {" ".join(palavra_oculta)}")
        print(f"Quantidade de erros: {erros}. \n")
    else:
        erros += 1
        print("*** Você errou, tente de novo!")
        print(f"Quantidade de erros: {erros}. \n")

print("-=" * 25)
if "_" not in palavra_oculta:
    print(f"VOCÊ VENCEU! A palavra era: {palavra}. \n")
else:
    print(f"VOCÊ PERDEU! A palavra era: {palavra} \n")