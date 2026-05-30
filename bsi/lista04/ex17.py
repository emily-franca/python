A = []
for i in range(128):
    numero = float(input(f"Digite o elemento {i}: "))
    A.append(numero)

#chave K
K = float(input("\nDigite a chave K: "))

#pesquisa Binária
inicio = 0
fim = len(A) - 1
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2  #índice meio
    if A[meio] == K:
        posicao = meio
        break
    elif K < A[meio]:
        fim = meio - 1  #procura metade esquerda
    else:
        inicio = meio + 1  #procura metade direita

if posicao != -1:
    print(f"\nCHAVE {K} encontrada na posição {posicao}.")
else:
    print(f"\nCHAVE {K} NÃO ENCONTRADA.")
