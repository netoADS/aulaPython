#criando uma lista de nomes
n = ['maria','josé','joão', 'ana','pedro']

n2 = []
e = 0
for i in n:
    e+=1
    if e <= len(n):
       n2.append(i.capitalize())
            

#ordenando a lista em ordem alfabética
n2.sort()

#imprimir a lista
print(n2)

ml = [8,10,6,2,4]
ml.sort()
print(ml)