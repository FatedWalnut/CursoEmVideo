nota1 = int(input('primeira nota? '))
nota2 = int(input('segunda nota ?'))
media = (nota1 + nota2)/2
if media >= 7:
    print('Aluno aprovado')
elif media < 5:
    print('Aluno reprovado')
elif media >= 5 and media < 7:
    print('Aluno em recuperação')

