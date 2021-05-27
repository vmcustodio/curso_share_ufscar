pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ").upper()
    if questão == 1 and resposta == "B":
        pontos = pontos + 1
    elif questão == 2 and resposta == "A":
        pontos = pontos + 1
    elif questão == 3 and resposta == "D":
        pontos = pontos + 1
    questão = questão + 1
print(f"O aluno fez {pontos} ponto(s)")
