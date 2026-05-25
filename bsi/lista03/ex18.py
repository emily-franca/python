preco_ini = 5.00
ingresso_ini = 200
despesas = 200.00

preco = 5.00
maior_lucro = 0
melhor_preco = 0
melhor_qtd_ingresso = 0

print("=" * 35)
print(f"{'Preço':<10} {'Ingressos':<12} {'Lucro'}")
print("-" * 35)

while preco >= 1.00:
    reducoes = int((preco_ini - preco) / 0.50)
    qtd = ingresso_ini + (reducoes * 26)
    lucro = (preco * qtd) - despesas

    print(f"R$ {preco:<6} {qtd:<12} R$ {lucro:.2f}")
    
    if lucro > maior_lucro:
        maior_lucro = lucro
        melhor_preco = preco
        melhor_qtd_ingresso = qtd

    preco -= 0.50

print("=" * 35)
print(f"\nLucro máximo: R$ {maior_lucro:.2f}")
print(f"Preço ideal: R$ {melhor_preco:.2f}")
print(f"Ingressos: {melhor_qtd_ingresso}")