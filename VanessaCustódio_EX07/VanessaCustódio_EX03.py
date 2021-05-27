L1 = [1,2,3,4,5]
L2 = [1,2,3]
L3 = L1
for item in L2:
    repetido = False
    for item1 in L3:
        if item == item1:
            repetido = True
            L3.remove(item)
            break
    if not repetido:
        L3.append(item)
print(L3)


