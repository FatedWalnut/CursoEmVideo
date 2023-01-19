nascimento = int(input('ANO DE NASCIMENTO ?:'))
atual = 2023
idade = atual - nascimento
if idade == 18:
    print('ESSE ANO TERÁ QUE SE ALISTAR:D')
elif idade < 18:
    print('AINDA FALTAM {} ANOS PARA SE ALISTAR SEU ALISTAMENTO SERÁ em {}'.format((18 - idade), (18 - idade)+ atual))
else:
    print('''     JÁ PASSOU DA HORA DE SE ALISTAR 
!!!!!FAZ {} ANOS QUE SE ATRASOU !!!!!'''.format(idade-18))