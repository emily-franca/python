DIARIA = 50.00

contas_encerradas = 0

while True:
    print("\n" + "=" * 30)
    print("          MENU DO HOTEL")
    print("=" * 30)
    print("1. Encerrar a conta de um hóspede")
    print("2. Verificar número de contas encerradas")
    print("3. Finalizar a execução")
    
    opcao = int(input("\nEscolha uma opção: "))
    
    if opcao == 1:
        nome = input("Nome do hóspede: ")
        diarias = int(input("Número de diárias: "))
        
        if diarias < 15:
            taxa = 7.50
        elif diarias == 15:
            taxa = 6.50
        else:  # diarias > 15
            taxa = 5.00
        
        total = (DIARIA + taxa) * diarias
        
        print("-" * 30)
        print(f"Hóspede: {nome}")
        print(f"Total a ser pago: R$ {total:.2f}")
        
        contas_encerradas += 1
    elif opcao == 2:
        print("-" * 40)
        print(f"Número de hóspedes que saíram: {contas_encerradas}")
    elif opcao == 3:
        print("\nSistema encerrado. Até mais!")
        break
    else:
        print("Opção inválida!")