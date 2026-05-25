while True:
    nome = input("Nome do cliente: ")
    
    if nome == "ULTIMO":
        break
    
    endereco = input("Endereço: ")
    valor_compra = float(input("Valor da compra (R$): "))
    
    if valor_compra > 500:
        desconto = valor_compra * 0.20
    else:
        desconto = valor_compra * 0.15
    
    total_pagar = valor_compra - desconto
    
    print("-" * 30)
    print(f"Cliente: {nome}")
    print(f"Valor original: R$ {valor_compra:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"TOTAL A PAGAR: R$ {total_pagar:.2f}")
    print("Para sair digite 'ULTIMO' \n")