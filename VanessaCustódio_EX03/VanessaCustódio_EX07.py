quantidadeKWh = int(input("Digite a quantidade de kWh consumida: "))
instalacao = (input("Digite o tipo de instalação: R para residencia, I para industria, C para comércio:  "))
if instalacao == "R":
    if quantidadeKWh <=500:
        preco = quantidadeKWh * 0.40
        print('O preço a pagar será de {}'.format(preco))
    else:
        preco = quantidadeKWh * 0.65
        print("O preço a pagar será de {}".format(preço))
elif instalacao == "C":
    if quantidadeKWh <=1000:
        preco = quantidadeKWh * 0.55
        print('O preço a pagar será de {}'.format(preco))
    else:
        preco = quantidadeKWh * 0.60
        print("O preço a pagar será de {}".format(preço))
elif instalacao == "I":
    if quantidadeKWh <=5000:
        preco = quantidadeKWh * 0.55
        print('O preço a pagar será de {}'.format(preco))
    else:
        preco = quantidadeKWh * 0.60
        print("O preço a pagar será de {}".format(preço))
else:
    print("Instalação inválida")