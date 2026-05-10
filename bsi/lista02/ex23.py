#Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa
#disciplina ao longo de um semestre, e calcule a sua média. O algoritmo deve mostrar na tela
#as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B
# ou C ou “REPROVADO” se o conceito for D ou E.
print("-----------------MÉDIA ALUNO-----------------")
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
print("---------------------------------------------")
#média
media = (n1+n2) / 2

#conceito
if media >= 9.0 and media <= 10:
    conceito = 'A'
elif media >= 7.5 and media < 9.0:
    conceito = 'B'
elif media >= 6.0 and media < 7.5:
    conceito = 'C'
elif media >= 4.0 and media < 6.0:
    conceito = 'D'
else:
    conceito = 'E'

#situação final
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    situacao = 'APROVADO!'
else:
    situacao = 'REPROVADO!'

print(f"Notas: {n1:.2f} e {n2:.2f}.")
print(f"Média: {media:.2f}.")
print(f"Conceito: {conceito}.")
print(f"Situação: {situacao}.")