soma_idades = 0
qtd = 0
res = 's'

while res == 's' or res == 'S':
    idade = int(input("Digite uma idade: "))
    
    if idade > 0:
        soma_idades += idade
        qtd += 1
    
    res = input("Deseja digitar mais um valor: s (SIM) / n (NAO)? ")

media = soma_idades / qtd

print("-" * 30)
print(f"Média de idade: {media:.2f} anos")
print(f"Total de pessoas válidas: {qtd}")