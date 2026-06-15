# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.
vogais = ["a", "e", "i", "o", "u"]
qtd_vogais = 0

frase = input("Digite a frase: ")
qtd_espaco = frase.count(" ")

frase.lower()

for v in vogais:
    qtd_vogais += frase.count(v)

print("-=" * 15)
print(f"Existem {qtd_espaco} espaços em branco.")
print(f"Quantide de vezes que aparecem vogais na frase: {qtd_vogais}. \n")