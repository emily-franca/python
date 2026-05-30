A = []
for i in range(128):
    num = float(input(f"Digite o elemento {i}: "))
    A.append(num)

K = float(input("\nDigite a chave K: "))

posicao = -1
for i in range(128):
    if A[i] == K:
        posicao = i
        break  

if posicao != -1:
    print(f"\nCHAVE {K} encontrada na posição {posicao}.")
else:
    print(f"\nCHAVE {K} NÃO ENCONTRADA.")
