#Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável composta chamada NOTA e calcule e imprima a sua média.
nota = []
media = 0

for i in range(10):
    nota.append(float(input(f"Digite a {i + 1}ª nota: ")))
media = sum(nota) / 10
print(f"{media:.2f}")
