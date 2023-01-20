import random
tentativa = 1
computador = random.randint(0, 10)
jogador =int(input('ESCOLHA UM NUMERO ENTRE 0 e 10'))
while jogador != computador:
    tentativa +=1
    jogador = int(input('ERROU!!!, TENTE NOVAMENTE'))
    print('ESSA FOI SUA {} TENTATIVA'.format(tentativa))
print('VOCE VENCEU!!!!, O NUMERO QUE PENSEI FOI {}, APÓS {} TENTATIVAS VOCE CONSEGUIU'.format(computador,tentativa))
if tentativa == 1:
    print('TU É BICHÃO MESMO EM CARA')
