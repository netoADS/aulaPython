#criando uma lista
ml = [1,2,3,4,5]


#usando um loop for para percorrer a lista e imprimir cada elemento
for i in range(len(ml)):
    print("O elemento", i+1, "da lista é: ", ml[i])

    
#criando uma lista de numeros
numeros = [1,2,3,4,5]


#usando um loop for para percorrer a lista e imprimir cada elemento
for n in numeros:
    print(n, ' - Com for')
    

#usando um loop while para percorrer a lista e imprimir cada elemento
i = 0

while i < len(numeros):
    print(numeros[i], ' - Com while')
    i +=1
    