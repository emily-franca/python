'''Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.'''

letra = input("Digite a letra para verificação: ")
letra = letra.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("VOGAL!")
else:
    print("CONSOANTE!")