vetor1 = []
vetor2 = []

print("VETOR 1:")
for i in range(25):
    num = float(input(f"{i+1}º elemento: "))
    vetor1.append(num)

print("\nDigite os 25 elementos do VETOR 2:")
for i in range(25):
    num = float(input(f"{i+1}º elemento: "))
    vetor2.append(num)

vetor3 = []
for i in range(25):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i]) 

print("\nRESULTAD0:")
for valor in vetor3:
    print(valor, end="  ")
print()
