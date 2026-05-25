acima20 = 0
tem18 = " "

for i in range(1, 4):
    nome = input(f"\nNome do {i}º aluno: ")
    idade = int(input(f"Idade: "))
    
    if idade == 18:
        tem18 += nome + " - "
    
    if idade > 20:
        acima20 += 1

print("\n" + "=" * 35)
print(f"Alunos com 18 anos: {tem18}")
print(f"Quantidade acima de 20 anos: {acima20}")