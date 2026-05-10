#Entrar com um número e informar se ele é divisível por 5.

num = int
(input("Digite o número para verificação: "))

res = num % 5

if res == 0:
  print(f"{num} é divisível por 5!")
else:
  print(f"{num} NÃO é divisível por 5!")
print("-----")