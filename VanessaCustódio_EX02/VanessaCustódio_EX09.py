qtdecigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Digite por quantos anos você fumou: "))
totalqtdecigarros = (anos *  365) * qtdecigarros
dias = (totalqtdecigarros*10)/24
print("você perdeu a quantidade de {:.2f} dias da sua vida por causa do cigarro".format(dias))