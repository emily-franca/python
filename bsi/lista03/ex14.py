#Faça um algoritmo que calcule e escreva o valor de pi usando os 51 primeiros termos da série.
soma = 0.0

for i in range(52):
    base = 2 * i + 1 #denominador ímpar
    fracao = 1 / (base **3) #fração completa

    #alternar o sinal da fração
    if i % 2 == 0:
        soma += fracao
    else:
        soma -= fracao
pi = (soma * 32) ** (1/3)
print(f"O valor de pi é: {pi}")