L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
v = int(input("Digite o valor a procurar:"))
x = 0
y = 0
while x < len(L):
    if L[x] == p:
        break
    x += 1
while y < len(L):
    if L[y] == v:
        break
    y += 1
if x>y:
    print("v foi encontrado antes")
else:
    print("p foi encontrado antes")
if x < len(L):
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")
if y < len(L):
    print(f"{v} achado na posição {y}")
else:
    print(f"{v} não encontrado")
