import datetime
maiores = 0
menores = 0
atual  = datetime.date.today().year
for i in range(7):
    nascimento = int(input('ano de nascimento {}'.format(i +1)))
    if atual - nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print('O numero de pessoas maiores é {} e o numero de pessoas menores é {}'.format(maiores, menores))
