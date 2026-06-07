nota = []
abaixo_media = 0

for i in range(30):
    nota.append(float(input(f"Digite a {i + 1}ª nota: ")))
media = sum(nota) / 30

for c in range (30):
    if nota[c] < media:
        abaixo_media += 1
print("-" * 30)
print(f"Maior nota: {max(nota)}")
print(f"Menor nota: {min(nota)}")
print(f"Média: {media:.2f}")
print(f"Quantidade de notas abaixo da média: {abaixo_media}")
