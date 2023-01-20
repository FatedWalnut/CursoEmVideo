sexo = input('QUAL SEU SEXO ?[M/F]:').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('DIGITOU ERRADO, REPITA O SEXO POR FAVOR [M/F]:').upper()
print('O SEXO SELECIONADO FOI {}'.format(sexo))