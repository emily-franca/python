#O programa deverá perguntar qual a temperatura que o alumínio deverá ser trabalhado e operar nas seguintes condições:
# • Se temperatura for inferior ou igual 500°C enviar uma mensagem para tela "Temperatura Inválida";
# • Se temperatura for menor do que 700°C enviar uma mensagem para tela "Aquecimento Ligado em 100%";
# • Se temperatura for menor do que 735°C enviar uma mensagem para tela "Aquecimento Ligado em 50%";
# • Se temperatura for maior ou igual 735°C enviar uma mensagem para tela "Aquecimento Desligado";
# • Se temperatura for maior do que 780°C enviar uma mensagem para tela "Superaquecimento";
# Os valores digitados devem ser inteiros e inferiores a 1000.

print("-------------->>TEMPERATURA FORNO<<--------------")
temp = int(input("Digite a temperatura para trabalhar (°C): "))

if temp >= 1000:
    print(">> Erro: A temperatura deve ser inferior a 1000°C.")
else:
    if temp <= 500:
        print(">> Temperatura Inválida")  
    elif temp < 700:
        print(">> Aquecimento Ligado em 100%")  
    elif temp < 735:
        print(">> Aquecimento Ligado em 50%")
    elif temp > 780:
        print("Superaquecimento")
    elif temp >= 735:
        print("Aquecimento Desligado")

