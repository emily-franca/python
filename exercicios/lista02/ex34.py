numero = int(input("Digite um número de 4 dígitos (1000 a 9999): "))

if numero < 1000 or numero > 9999:
    print("Erro: O número deve ter exatamente 4 dígitos.")
else:
    # Decomposição   
    parte1 = numero // 100
    parte2 = numero % 100
    
    soma = parte1 + parte2
    quadrado_da_soma = soma ** 2
    
    print(f"Dividindo {numero}: {parte1} e {parte2}")
    print(f"Soma: {parte1} + {parte2} = {soma}")
    print(f"Quadrado da soma: {soma}² = {quadrado_da_soma}")
    
    if quadrado_da_soma == numero:
        print(f"\nO número {numero} OBEDECE à característica!")
    else:
        print(f"\nO número {numero} NÃO obedece à característica.")