num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('ESCOLHA UM NUMERO [999 PARA]:'))
    if num == 999:
        break
    soma += num
    cont += 1
print('A SOMA DOS NÚMEROS É {} E VOCE DIGITOU {} '.format(soma, cont))