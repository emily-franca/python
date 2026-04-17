#26. Faça um algoritmo que leia 3 valores a, b, c, e verifique se podem ser os
# comprimentos dos lados de um triângulo. Em caso afirmativo, verifique se é “triângulo
# equilátero”, “triângulo isósceles” ou “triângulo escaleno”. Em caso negativo, escreva
# uma mensagem: “os valores lidos não formam um triângulo”. Considere que:
# • o comprimento de cada lado de um triângulo é menor que a soma dos comprimentos dos outros lados
# • um triângulo equilátero tem três lados iguais
# • um triângulo isósceles tem dois lados iguais e um diferente
# • um triângulo escaleno tem três lados diferentes.

a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b == c:
        print("Triângulo EQUILÁTERO.")
    elif a == b or a == c or b == c:
        print("Triângulo ISÓSCELES.")
    else:
        print("Triângulo ESCALENO.")
else:
    print("Os valores lidos não formam um triângulo.")