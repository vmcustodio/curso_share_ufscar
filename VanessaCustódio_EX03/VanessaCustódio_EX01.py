velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 80:
    preco = (velocidade-80)*5
    print("Você foi multado, com o valor de R$ {}".format(preco))
else:
    print('Você não foi multado')