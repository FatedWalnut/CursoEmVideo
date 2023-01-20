n = int(input('QUER VER A TABUADA DE QUAL VALOR ?:'))
fim = 1
while n >= 0:
    for i in range(1,11):
        conta = i * n
        print('{} x {} = {} '.format(i, n, conta))
    n = int(input('QUER VER A TABUADA DE QUAL VALOR ?:'))
