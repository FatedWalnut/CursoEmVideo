import random as rd
jogador = int(input('SELECIONE UM NUMERO DE 0 A 10'))
computador = rd.randint(0, 10)
tipo = ' '
venceu = 0
total = jogador + computador
while tipo not in 'PI':
    tipo = input('PAR OU IMPAR [P/I]').strip().upper()[0]
    print('VOCE JOGOU {} E O COMPUTADOR {} TOTALIZANDO {}'.format(jogador, computador, total))
    if tipo == 'P':
        if total % 2 == 0:
            venceu += 1
            print('PARABENS VOCE GANHOU {} SEGUIDAS'.format(venceu))
        else:
            print('VOCE PERDEU HAHA')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('VOCE PERDEU HAHA')
            break
        else:
            venceu += 1
            print('PARABENS VOCE GANHOU {} SEGUIDAS'.format(venceu))
    print('VAMOS JOGAR NOVAMENTE')
    jogador = int(input('SELECIONE UM NUMERO DE 0 A 10'))
    tipo = ' '
    total = jogador + computador
print('ACABOU')