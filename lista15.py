ml = []
trocado = True
num = int(input('quantos elementos deseja? '))

for i in range(num):
    val = float(input('Entre com o número: '))
    ml.append(val)
    
while trocado:
    trocado = False
    for i in range(len(ml) - 1):
        if ml[i] > ml[i + 1]:
            trocado = True
            ml[i], ml[i + 1] = ml[i + 1], ml[i]
            
print('\nOrdenado: ')
print(ml)