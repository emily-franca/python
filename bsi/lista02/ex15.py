#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor
#da compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o
#valor do produto e imprimir o valor da venda.

valor_produto = float(input("Digite o valor do produto: "))
if valor_produto < 20:
    lucro = (valor_produto * 45) / 100
    valor_venda = valor_produto + lucro
else:
    lucro = (valor_produto * 30) / 100
    valor_venda = valor_produto + lucro
print(f"O valor de venda é: R${valor_venda}")