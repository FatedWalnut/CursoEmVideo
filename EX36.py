valor = float(input('QUANTO CUSTA O IMOVEL???:'))
salario = float(input('QUAL O SEU SALARIO ??:'))
tempo = int(input('EM QUANTOS ANOS PRETENDE QUITAR O IMOVEL???: ')) *12
if (valor / tempo) >(salario * 0.3):
    print(f'EMPRESTIMO NEGADO, VOCE DEVERIA RECEBER NO MINIMO {(((valor/tempo)*100)/30) } ')
else:
    print('EMPRESTIMO APROVADO')

