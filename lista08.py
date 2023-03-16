#criando uma lista com elementos duplicados
lcd = [1,2,3,1,4,2,5,6,3,7,8,5,9]

#inicializando uma lista vazia para armazenar os elementos unicos
lsd = []

#usando um loop while para percorrer a lista e remover os elementos duplicados
while lcd:
    e = lcd.pop(0) #pop é usada para remover o elemento
    if e not in lsd:
        lsd.append(e)
        
#imprimindo o resultado
print('a lista sem duplicatas é:', lsd)