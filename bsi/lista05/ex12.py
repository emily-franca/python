print(".:: Valida e corrige número de telefone ::. \n")

telefone = input("Informe o número de telefone: ")

telefone_limpo = telefone.replace("-", "")

if telefone_limpo.isdigit():
    if len(telefone_limpo) == 7:
        print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente! \n")
        telefone_corrigido = "3" + telefone_limpo
    elif len(telefone_limpo) == 8:
        telefone_corrigido = telefone_limpo
    else:
        print("*** Número inválido! Deve ter 7 ou 8 dígitos. \n")
        telefone_corrigido = None
    
    if telefone_corrigido:
        print("-=" * 20)
        print(f"Telefone corrigido sem formatação: {telefone_corrigido}.")
        print(f"Telefone corrigido com formatação: {telefone_corrigido[:4]}-{telefone_corrigido[4:]} \n")
else:
    print("*** Número  inválido! Deve conter apenas dígitos. \n")
