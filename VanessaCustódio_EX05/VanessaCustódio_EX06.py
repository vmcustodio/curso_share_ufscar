valor = float(input("Digite o valor a pagar:"))
cédulas = 0
atual = 100
apagar = valor
while valor != 0:
    while True:
        if atual <= apagar:
            apagar = float("{:.2f}".format(apagar - atual))
            cédulas += 1
        else:
            print(f"{cédulas} cédula(s) de R${atual}")
            if apagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01
            cédulas = 0
    valor = float(input("digite o valor a pagar: "))
    cedulas = 0
    atual = 100
    apagar= valor