ultimo = 1
fila = list(range(1, ultimo + 1))
print(f"\nExistem {len(fila)} clientes na fila")
print(f"Fila atual: {fila}")
print("Digite F para adicionar um cliente ao fim da fila,")
print("ou A para realizar o atendimento. S para sair.")
operacoes = input("Operações (F, A ou S):")
for operacao in operacoes:
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido.")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao == "F":
        ultimo += 1 # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")