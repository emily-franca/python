VET = []
for i in range(20):
    num = float(input(f"Digite o {i+1}º número: "))
    VET.append(num)

VET.sort()

print("\nRESULTADO:")
for x in VET:
    print(f"{x:.2f}", end=" ")
print()
