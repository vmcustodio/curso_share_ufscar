mercadoria = float(input("digite o preço da mercadoria: R$"))
desconto = float(input("digite o desconto % : "))
novovalor = (mercadoria- (mercadoria*(desconto/100)))
totaldesconto = mercadoria-novovalor
print("o novo valor da mercadoria será de R${}, com o desconto de {}".format(novovalor,totaldesconto))