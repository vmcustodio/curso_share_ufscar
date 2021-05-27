distancia = int(input('Qual distancia você deseja percorrer em km?: '))
if distancia <= 200:
    preço = distancia * 0.50
    print('O preço da passagem será de {}'.format(preço))
else: 
    preço = distancia * 0.45
    print('O preço da passagem será de {}'.format(preço))