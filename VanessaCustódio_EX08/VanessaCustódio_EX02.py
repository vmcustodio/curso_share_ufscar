ultimo1 = 1
ultimo2 = 1
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 +1))
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1")
    print(f"\nExistem {len(fila2)} clientes na fila 2")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da fila 1,")
    print("ou A para realizar o atendimento. S para sair.")
    print("Digite G para adicionar um cliente ao fim da fila 2,")
    print("ou B para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, G, A, B ou S):")
    if operacao == "A":
        if len(fila1) > 0:
            atendido = fila1.pop(0)
            print(f"Cliente {atendido} atendido.")
        else:
            print("Fila 1 vazia! Ninguém para atender.")
    elif operacao == "B":
        if len(fila2) > 0:
            atendido = fila2.pop(0)
            print(f"Cliente {atendido} atendido.")
        else:
            print("Fila 2 vazia! Ninguem para atender.")
    elif operacao == "F":
        ultimo1 += 1 # Incrementa o ticket do novo cliente
        fila1.append(ultimo1)
    elif operacao == "G":
        ultimo2 += 1 
        fila2.append(ultimo2)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, G, B, A ou S!")