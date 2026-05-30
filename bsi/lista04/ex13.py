frase = input("Digite uma frase (máx. 50 caracteres): ")[:50]

# espaços em branco
qtd_brancos = frase.count(" ")

#quantas vezes a letra A aparece
qtd_A = frase.upper().count("A")

print("\nQuantidade de espaços em branco:", qtd_brancos)
print("Quantidade de letras 'A':", qtd_A)
