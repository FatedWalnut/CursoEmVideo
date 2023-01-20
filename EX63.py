n = int(input('POSIÇÂO DA SEQUENCIA:'))
pos1 = 0
pos2 = 1
print('{} -> {}'.format(pos1, pos2), end = ' ')
cont = 3
while cont <= n:
    pos3 = pos1 + pos2
    print(' -> {}'.format(pos3), end =' ')
    pos1 = pos2
    pos2 = pos3
    cont += 1

