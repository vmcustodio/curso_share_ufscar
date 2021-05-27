salario = float(input('Digite o valor do salario: R$'))
if salario > 1250.00:
    aumento = salario*0.1
    novosalario = salario + (aumento)
    print('O aumento será de R$ {}, tendo o novo salario de R$ {}'.format(aumento,novosalario))
else: 
    aumento = salario*0.15
    novosalario = salario + (aumento)
    print('O aumento será de R$ {}, tendo o novo salario de R$ {}'.format(aumento,novosalario))