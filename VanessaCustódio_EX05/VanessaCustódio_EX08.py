opcao = int(input("Digite a opção desejada: 1 para adição, 2 para subtração, 3 para divisão, 4 para multiplicar e 5 para sair: "))
cont = 1
while True:
    if opcao == 5 or opcao>5:
        break
    numero = int(input("Digite a tabuada de qual número você deseja: "))  
    while cont <= 10:
        if opcao ==1:
            print(f"{numero}+{cont}={cont+numero}")
        elif opcao ==2:
            print(f"{numero}-{cont}={numero-cont}")
        elif opcao ==3:
            print(f"{numero}/{cont}={numero/cont}")
        else:
            print(f"{numero}*{cont}={cont*numero}")
        cont +=1
    opcao = int(input("Digite a opção desejada: 1 para adição, 2 para subtração, 3 para divisão, 4 para multiplicar e 5 para sair"))
    cont = 1