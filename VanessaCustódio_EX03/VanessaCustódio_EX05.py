a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
escolha = int(input('Digite 1 para divisão, 2 para multiplicação, 3 para soma, 4 para subtração: '))
if escolha == 1:
    resultado = a/b
    print(a, '/',b,"=",resultado)
elif escolha == 2:
    resultado = a*b
    print(a, '*',b,"=",resultado)
elif escolha == 3:
    resultado = a+b
    print(a, '+',b,"=",resultado)
elif escolha == 4:
    resultado = a-b
    print(a, '-',b,"=",resultado)
else:
    print('Operação invalida')