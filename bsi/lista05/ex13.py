import random

print(".:: JOGO DA PALAVRA EMBARALHADA ::. \n")

palavras = ["python", "programacao", "livro", "estudar"]
palavra = random.choice(palavras)

lista_letras = list(palavra) # transforma em uma lista para dps embaralhar
random.shuffle(lista_letras)
embaralhada = "".join(lista_letras)

print(f"A palavra embaralhada é: {embaralhada}\n")

tentativas = 6
acertou = False

while tentativas > 0 and not acertou:
    res = input("Qual é a palavra? ").lower()

    if res == palavra:
        acertou = True
    else:
        tentativas -= 1
        print(f"*** Errado! Restam {tentativas} tentativas. \n")

print("-=" * 25)
if acertou:
    print(f"VOCÊ ACERTOU! A palavra era: {palavra}. \n")
else:
    print(f"VOCÊ PERDEU! A palavra era: {palavra}. \n")