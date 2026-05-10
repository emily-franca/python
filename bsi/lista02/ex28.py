#Uma empresa decidiu conceder um aumento de salário a seus funcionários de acordo com a tabela:
# em R$ Índice de Aumento
# salário £ 400.00 15%
# 400.00 < salário £ 700.00 12%
# 700.00 < salário £ 1000.00 10%
# 1000.00 < salário £ 1500.00 7%
# 1500.00 < salário £ 2000.00 4%
# salário > 2000.00 sem aumento
# Faça um algoritmo que leia o salário atual de um funcionário e escreva o índice de aumento e o valor do salário corrigido.

salario_atual = float(input("Digite o salário atual do funcionário: R$"))
indice = 0

if salario_atual <= 400.00:
    indice = 15
elif salario_atual <= 700.00:
    indice = 12
elif salario_atual <= 1000.00:
    indice = 10
elif salario_atual <= 1500.00:
    indice = 7
elif salario_atual <= 2000.00:
    indice = 4
else:
    indice = 0

aumento = (salario_atual * indice) / 100
novo_salario = salario_atual + aumento

print("-" * 20)
if indice > 0:
    print(f"Índice: {indice}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")
else:
    print("Salário maior que R$ 2000.00. Não há previsão de aumento.")
print("-" * 20)