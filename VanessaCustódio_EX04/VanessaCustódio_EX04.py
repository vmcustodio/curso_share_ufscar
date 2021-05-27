inicio = int(input('Digite o inicio da tabuada :'))
fim = int(input("Digite o fim da tabuada: "))
x = inicio
while x <= fim:
    tabuada = 1
    while tabuada <= 10:
        print(f"{x} X {tabuada} = {x*tabuada}")
        tabuada += 1 
    x += 1
    print()



