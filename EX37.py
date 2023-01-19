numero = int(input('DIGITE O NUMERO INTEIRO'))
print('''ESCOLHA  UMA DAS BASES PARA CONVERSÂO:
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL''')
opcao = int(input('SUA OPÇÂO ?:'))
if opcao == 1:
    print('{}  convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))

elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)))
else:
    print('!!!!!OPÇÂO INVALIDA!!!!!!')
