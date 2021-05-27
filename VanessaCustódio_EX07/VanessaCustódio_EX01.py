L1 = []
L2 = []
L3 = []
lista1 = input("Escreva numeros separados por espaço e aperte enter para confirmar")
for item in lista1.split():
    L1.append(item)
lista2 = input("Escreva numeros separados por espaço e aperte enter para confirmar")
for item1 in lista2.split():
    L2.append(item1)
L3.extend(L1)
L3.extend(L2)
print(L3)