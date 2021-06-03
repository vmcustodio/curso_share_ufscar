T = [-10, -8, 0, 1, 2, 5, -2, -4]
menorTemp = T[0]
maiorTemp = T[0]
media = 0
for e in T:
    if e < menorTemp:
        menorTemp = e
print(menorTemp)
for e in T:
    if e > maiorTemp:
        maiorTemp = e
print(maiorTemp)
media = sum(T)/len(T)
print(media)