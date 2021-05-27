valores = (input("Digite três valores: ")).split()
a, b, c = valores  
maior_entre_aeb = (int(a)+int(b)+abs(int(a)-int(b)))/2
maiortotal = (int(maior_entre_aeb)+int(c)+abs(int(maior_entre_aeb)-int(c)))/2
print(int(maiortotal))