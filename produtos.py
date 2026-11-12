produtos = [
    [1, "Camiseta", 49.90],
    [2, "Bermuda", 79.90],
    [3, "Boné", 35.00]
]

print("Produtos:", produtos)

for p in produtos:
    if p[0] == 1:
        p[2] = 55.00

for p in produtos:
    if p[0] == 1:
        print("Id 1:", p)

for p in produtos:
    if p[0] == 3:
        produtos.remove(p)

produtos.append([4, "Meia", 15.00])
print("Produtos:", produtos)
