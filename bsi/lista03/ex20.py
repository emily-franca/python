hora = 1
quebrados = 1

print("=" * 30)
print("Biscoitos quebrados por hora")
print("-" * 30)

for hora in range(1, 17):
    print(f"{hora}:00h: {quebrados} biscoitos quebrados")

    quebrados *= 3
print("=" * 30)
print(f"\nTotal no dia: {quebrados // 3} biscoitos")