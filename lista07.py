#criando uma lista de números
n = [10,20,30,40,50]

#inicializando a variavel que ira armazenar o maior numero
mn = n[0]

#usando um loop for para percorrer a lista e encontrar o maior numero
for i in n:
    if i > mn:
        mn = i
        
#imprimindo o resultado
print('O maior número na lista é', mn)