import random as rd
jogador = 0
print('Vamos JOGAR JAKENPÔ')
while jogador == 0:
    jogada_jogador = int(input('ESCOLHA : PAPEL = 0, PEDRA = 1, TESOURA = 2'))
    jogada_computador = rd.randint(0,2)
    if jogada_jogador == 0 and jogada_computador == 1 or \
        jogada_jogador == 1 and jogada_computador == 2 or\
        jogada_jogador == 2 and jogada_computador == 0:
        print('VOCE VENCEU:D')
    elif jogada_jogador == jogada_computador:
        print('EMPATAMOS :|')
    elif jogada_computador == 0 and jogada_jogador == 1 or \
        jogada_computador == 1 and jogada_jogador == 2 or\
        jogada_computador == 2 and jogada_jogador == 0:
        print('VENCI SEU ANIMAL RETARDADO')
    jogador = int(input('QUER JOGAR NOVAMENTE? SE SIM APERTE o ZERO(0)'))
