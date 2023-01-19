
primos = 0
primo = int(input('ESCOLHA UM NUMERO:'))
for i in range(primo):
    if primo % (i+1) == 0:
        primos +=1
if primos == 2:
    print('É primo')
else:
    print('NÂO É PRIMO')