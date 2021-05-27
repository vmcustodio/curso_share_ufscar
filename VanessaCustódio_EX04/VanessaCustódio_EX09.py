depositoInicial = float(input("Digite o deposito inicial: "))
depositoMensal = float(input("Digite o deposito mensal: "))
juros = float(input("Digite a taxa de juros: " ))/100
cont = 1
acumulador = 0
while cont <= 24:
    ganho = depositoInicial * juros
    acumulador += ganho
    depositoInicial += ganho 
    print(f"mês {cont}, com o juro desse mes de R${ganho:.2f} e total na conta de R$ {depositoInicial:.2f}")
    cont +=1 
    depositoInicial += depositoMensal
print(f"total de juros ganhado no periodo de R${acumulador:.2f}")