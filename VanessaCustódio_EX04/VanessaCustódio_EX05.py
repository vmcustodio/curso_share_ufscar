x1 = int(input('digite o primeiro numero: '))
x2 = int(input('digite o segundo numero: '))
cont = 1
resultado = 0
while cont <= x1:
    resultado += x2
    cont += 1
    print(resultado)
print(f"{x1} X {x2} = {resultado}")