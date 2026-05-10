#Faça um algoritmo para calcular o reajuste salarial de um funcionário, de acordo com os critérios abaixo:
# • se salário é inferior a R$ 10.000,00 deve ter um reajuste de 55%
# • se salário está entre R$ 10.000,00 (inclusive) e R$ 25.000,00 (inclusive) deve ter um reajuste de 20%
# • se salário é superior a R$ 25.000,00 deve ter um reajuste de 20%.

sal_atual = float(input("Digite o salário atual: "))

if sal_atual < 10000.00:
    reajuste = (sal_atual * 55) / 100
elif sal_atual >= 10000.00 and sal_atual <= 25000.00:
    reajuste = (sal_atual * 20) / 100
else:
    reajuste = (sal_atual * 20) / 100
sal_final = sal_atual + reajuste
print("-" * 5)
print(f"Valor do reajuste: R${reajuste:.2f}")
print(f"Salário final: R${sal_final:.2f}")