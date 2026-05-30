nota = []
acima_media = []
media = 0

for i in range(10):
    nota.append(float(input(f"Digite a {i + 1}ª nota: ")))
media = sum(nota) / 10

for c in range (10):
    if nota[c] > media:
        acima_media.append(nota[c])
print("-" * 30)
print(f"Média: {media:.2f}")
print(f"Quantidade de notas acima da média: ", len(acima_media))