numero = 1
cont = 0
soma = 0
media = 0
while numero != 0:
    numero = int(input("Digite um numero: "))
    soma += numero
    cont += 1
media = soma/cont
print(f"Foram digitados {cont} numeros com média aritmétics de {media}, e soma de {soma}")  