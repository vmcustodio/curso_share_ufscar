dividaInicial = float(input("Digite o valor da divida: R$"))
jurosMensal = float(input("Digite o juros mensal: "))/100
valorMensal = float(input("Digite o valor mensal pago: R$"))
meses = 0
valorPago = 0
acumulador = 0
while dividaInicial > 0:
    dividaInicial -= valorMensal
    acumulador += dividaInicial * jurosMensal
    dividaInicial += jurosMensal*dividaInicial
    valorPago += valorMensal 
    meses += 1
print(f"levaram {meses} meses para quitar a divida, foi pago o total de {valorPago+dividaInicial:.2f} com o juros de {acumulador:.2f}")
