numero = int(input("Digite um numero pra descobrir se ele é um número primo: "))
cont = 3
if numero == 2:
    print("Você digitou um numero primo")
elif numero % 2 ==0:
    print("Você digitou um numero par, logo ele não é primo")
else:
    while cont < numero:
        x = numero%cont
        cont+=2
        if x == 0:
            print("O numero que você digitou não é primo")
            break
    if cont==numero:
        print("O número que você digitou é primo")
