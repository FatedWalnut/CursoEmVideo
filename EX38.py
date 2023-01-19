numero1 = int(input('primeiro numero?:'))
numero2 = int(input('segundo numero?:'))
if numero1 > numero2:
    print('o primeiro número {} é maior que o segundo número {}'.format(numero1, numero2))
elif numero2 > numero1:
    print('o segundo número: {} é maior que o primeiro número: {}'.format(numero2, numero1))
else:
    print(' os dois são iguais')