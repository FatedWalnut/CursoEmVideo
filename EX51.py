primeiro = int(input('primeiro termo:'))
razao = int(input('razão da PA:'))
print(primeiro)
for i in range(9):
    primeiro += razao
    print(primeiro)