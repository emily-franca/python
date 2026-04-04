'''10. Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra
“Aprovado” se a média das duas notas for maior ou igual a 7,0. Caso a média seja
inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta
média for maior ou igual a 5,0, o programa deve escrever “Aprovado”, caso contrário
deve escrever “Reprovado”.'''

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota:"))

media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado!")
else:
    nota_exame = float(input("Digite a nota do exame: "))
    #assumindo que a nota mais baixa será substituida pela nota do exame:
    if nota_exame >= n1:
        n1 = nota_exame
    elif nota_exame >= n2:
        n2 = nota_exame
    media_exame = (n1 + n2) / 2

    if media_exame >= 5:
        print("Aprovado!")
    else:
        print("Reprovado!")