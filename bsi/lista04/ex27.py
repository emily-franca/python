estoque = [
    [1200, 3700, 3737],  # Armazém 1
    [1400, 4210, 4224],  # Armazém 2
    [2000, 2240, 2444]   # Armazém 3
]

custos = [260.00, 420.00, 330.00]

print("Itens em cada armazém:")
for i in range(3):
    total_armazem = sum(estoque[i])
    print(f"Armazém {i+1}: {total_armazem} itens")

produto2 = [estoque[i][1] for i in range(3)]
maior_armazem = produto2.index(max(produto2)) + 1
print(f"\nArmazém com maior quantidade de Produto 2: Armazém {maior_armazem}")

print("\nCusto de cada produto em cada armazém:")
for i in range(3):  # armazéns
    for j in range(3):  # produtos
        custo_produto = estoque[i][j] * custos[j]
        print(f"Armazém {i+1}, Produto {j+1}: R$ {custo_produto:,.2f}")

print("\nCusto total em cada armazém:")
for i in range(3):
    custo_armazem = sum(estoque[i][j] * custos[j] for j in range(3))
    print(f"Armazém {i+1}: R$ {custo_armazem:,.2f}")

print("\nCusto total de cada produto em todos os armazéns:")
for j in range(3):
    custo_produto_total = sum(estoque[i][j] for i in range(3)) * custos[j]
    print(f"Produto {j+1}: R$ {custo_produto_total:,.2f}")
