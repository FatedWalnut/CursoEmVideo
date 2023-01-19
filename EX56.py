idade = 0
homem = 0
mulher = 0
idades = 0
velho = 0
for i in range(1, 5):
    print('------ {} ------'.format(i))
    nome = input('NOME:').upper()
    idade = int(input('IDADE:'))
    sexo = input('[M/F]:').upper()
    if sexo == 'M':
        if idade > velho:
            velho = idade
            homem = nome
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    idades += idade
print(f'A MÉDIA DE IDADE DO GRUPO é {idades/4}, O HOMEM MAIS VELHO SE CHAMA {homem} E O NUMERO DE MULHERES MENORES DE 20 ANOS é {mulher} ')

