soma = 0
for i in range(6):
    num= int(input('{} numero ?:'.format(i+1)))
    if num % 2 == 0:
        soma += num
print(soma)