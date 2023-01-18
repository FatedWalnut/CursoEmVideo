preco = float(input('PREÇO DO PRODUTO'))
pagamento = int(input('TIPO DE PAGAMENTO : à vista em dinheiro(0), à vista cartão(1), 2xcartão(2), 3x ou maix no cartão(3)'))
if pagamento == 0:
    print(f'preço final R$:{preco*0.9}')
elif pagamento == 1:
    print(f'preço final R$:{preco*0.95}')
elif pagamento == 2:
    print(f'preço final R$:{preco}')
elif pagamento == 3:
    print(f'preço final R$:{preco*1.20}')
