x = int(input("Digite um numero pra imprimir essa quantidade de numeros primos: "))
qtdePrimos = 0
numero = 2
while qtdePrimos < x:
    cont = 3
    if numero ==2:
        print(numero)
        qtdePrimos +=1
    elif not(numero % 2 ==0):
        while cont < numero:
            resto = numero%cont
            cont+=2
            if resto == 0:
                break
        if cont==numero:
            print(numero)
            qtdePrimos +=1
    numero +=1
    