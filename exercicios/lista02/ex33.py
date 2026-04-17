#idade dos homens
h1 = int(input("Digite a idade do primeiro homem: "))
h2 = int(input("Digite a idade do segundo homem: "))

#idade das mulheres
m1 = int(input("Digite a idade da primeira mulher: "))
m2 = int(input("Digite a idade da segunda mulher: "))

#homem mais velho e o mais novo
if h1 > h2:
    h_velho = h1
    h_novo = h2
else:
    h_velho = h2
    h_novo = h1

#mulher mais velha e a mais nova
if m1 > m2:
    m_velha = m1
    m_nova = m2
else:
    m_velha = m2
    m_nova = m1

soma = h_velho + m_nova
produto = h_novo * m_velha

print("-" * 30)
print(f"Homem mais velho: {h_velho} anos | Mulher mais nova: {m_nova} anos")
print(f"Soma (Homem Velho + Mulher Nova): {soma}")
print("-" * 30)
print(f"Homem mais novo: {h_novo} anos | Mulher mais velha: {m_velha} anos")
print(f"Produto (Homem Novo * Mulher Velha): {produto}")
print("-" * 30)