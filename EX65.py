num = int(input('DIGITE UM NUMERO:'))
continuar = input('CONTINUAR [S/N]').upper()
cont = 1
media, maior, menor, soma = num, num, num, num
while continuar == 'S':
    num = int(input('DIGITE UM NUMERO:'))
    soma += num
    cont +=1
    if menor > num:
        menor = num
    if maior < num:
        maior = num
    media = soma / cont
    continuar = input('CONTINUAR [S/N]').upper()
print('A SOMA DE TODOS FORAM {}, O MAIOR NUMERO FOI {}, O MENOR NUMERO FOI {}, E A MÉDIA FOI DE {}'.format(soma, maior, menor, media))

