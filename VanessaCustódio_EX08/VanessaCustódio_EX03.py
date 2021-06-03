parenteses = input("")
pilha = []
erro = False
for x in range(len(parenteses)):
    if parenteses[x] == "(":
        pilha.append(parenteses[x])
    else:
        if len(pilha) == 0:
            erro = True
            break
        if pilha[-1] == "(":
            pilha.pop()
        else:
            erro = True
            break
if not erro:
    print("OK")
else:
    print("ERRO")