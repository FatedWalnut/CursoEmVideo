maior = 0
menor = 0
for i in range(1,6):
    peso = float(input('PESO DA {} pessoa'.format(i)))
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(' O MAIOR PESO LIDO FOI DE {}KG'.format(maior))
print(' O MENOR PESO LIDO FOI DE {} KG'.format(menor))