codigo = 0
quantidadeComprada = 0
totalCompras = 0
preco = 0
while True:
    codigo = int(input("Digite o código do produto: "))
    quantidadeComprada = int(input("Digite a quantidade comprada: "))
    if codigo == 1:
        preco =(quantidadeComprada*0.50)
    elif codigo ==2:
        preco=(quantidadeComprada*1)
    elif codigo == 3:
        preco=(quantidadeComprada*4)
    elif codigo == 5:
        preco=(quantidadeComprada*7)
    elif codigo == 9:
        preco=(quantidadeComprada*8)
    else:
        print("código invalido")
        break
    totalCompras += preco
print(f"O total será de R${totalCompras}")
