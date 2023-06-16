cadastrar = input('DESEJA CADASTRAR ALGUMA PESSOA[S/N]').strip().upper()[0]
menor = 0
maior = 0
pessoas = 0
homem = 0
while cadastrar == 'S':
    idade = int(input('IDADE:'))
    sexo = input('SEXO [M/F]')
    if sexo == 'F' and idade <= 20:
        menor += 1
        pessoas += 1
    elif idade > 18:
        maior += 1
        pessoas += 1
    elif sexo == 'M':
        homem += 1
        pessoas += 1
    else:
        pessoas += 1
    cadastrar = input('DESEJA CADASTRAR ALGUMA PESSOA[S/N]').strip().upper()[0]
print('FORAM CADASTRADOS {} PESSOAS, {} MULHERES MENORES DE 20, {} HOMENS E {} PESSOAS MAIORES DE 18 '.format(pessoas, menor, homem, maior))
