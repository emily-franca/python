qtd = []
preco = []

print("Digite as quantidades vendidas de cada mercadoria (0 a 99):")
for i in range(100):
    q = int(input(f"Quantidade da mercadoria {i}: "))
    qtd.append(q)

print("\nDigite os preços de venda de cada mercadoria (0 a 99):")
for i in range(100):
    p = float(input(f"Preço da mercadoria {i}: "))
    preco.append(p)

#faturamento mensal
faturamento = 0
for i in range(100):
    faturamento += qtd[i] * preco[i]

print("\nFATURAMENTO MENSAL =", faturamento)
