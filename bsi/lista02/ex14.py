#Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: “Carioca,
#Paulista, Mineiro ou Outros”

sigla = input("Digite a sigla do seu estado: ")
#Deixando a string em uppercase
sigla = sigla.upper()
if sigla == 'RJ':
    print("Carioca!")
elif sigla == 'SP':
    print("Paulista!")
elif sigla == 'MG':
    print("Mineiro(a)!")
else:
    print("Outros...")