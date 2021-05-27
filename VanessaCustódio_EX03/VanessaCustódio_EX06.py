casaValor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
qtdAnos = int(input('Digite a quantidade anos a pagar: '))
prestacao = casaValor/ (qtdAnos/12)
if prestacao > (salario*0.3):
    print('Você não pode comprar a casa!')
else: 
    print('Você pode comprar a casa!')