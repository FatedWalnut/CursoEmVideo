primeiro = int(input('ESCOLHA O PRIMEIRO VALOR:'))
segundo = int(input('ESCOLHA O SEGUNDO VALOR:'))
sair = 0
conta = 0
while sair != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR''')
    sair = int(input())
    if sair == 1:
        conta = primeiro + segundo
        print('{} + {} = {}'.format(primeiro,segundo,conta))
    if sair == 2:
        conta = primeiro * segundo
        print(' {} * {} = {}'.format(primeiro, segundo, conta))
    if sair == 3:
        if primeiro > segundo:
            print('O PRIMEIRO VALOR {} É >   {}'.format(primeiro, segundo))
        else:
            print('O SEGUNDO VALOR {} É >  {}'.format(segundo, primeiro))
    if sair == 4:
        primeiro = float(input('ESCOLHA NOVAMENTE O PRIMEIRO VALOR'))
        segundo  = float(input('ESCOLHA NOVAMENTE O SEGUNDO VALOR'))

print('!!!FIM!!!')