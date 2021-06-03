# Programa - Adicao de elementos a lista
L = []
while True:
    n = int(input("Digite um numero (0 sai):"))
    if n == 0:
        break
    L.append(n)
x = 0
for x in range (len(L)):
    print(L[x])
    x+=1
# nem todos os whiles conseguem ser transformados em for (principalmente os whiles True), pois na forma de repetição for, sabe-se a quantidade de vezes que irá acontecer a repetição, ao contrario da repetição while.