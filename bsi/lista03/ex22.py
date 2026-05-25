soma_altura = 0
soma_altura_m = 0
qtd_m = 0

n = int(input("Quantidade de pessoas para cadastrar: "))

for i in range(n):
    print(f"--{i+1}ª PESSOA--")
    altura = float(input("Altura (m): "))
    sexo = input("Sexo (f / m): ")
    #validação
    if sexo == 'M':
        sexo = 'm'
    if sexo == 'F':
        sexo = 'f'
    soma_altura += altura

    if sexo == 'f':
        soma_altura_m += altura
        qtd_m += 1
print("-" * 6)
print(f"Média da altura das mulheres: {soma_altura_m / qtd_m:.2f}")
print(f"Média de altura da turma: {soma_altura / n:.2f}")