fator = int(input('ESCOLHA UM NÚMERO PARA VER SEU FATORIAL'))
conta = fator - 1
fatorial = fator
while conta >= 1:
    fatorial = fatorial * conta
    conta -= 1
print('{}! = {}'.format(fator,fatorial))