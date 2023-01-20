primeiro = int(input('primeiro termo:'))
razao = int(input('razão da PA:'))
contador = 10
while contador >= 0:
    primeiro += razao
    print(primeiro)
    contador -= 1
    if contador == 0:
        contador = int(input(' VAI QUERER MOSTRAR MAIS QUANTOS TERMOS?:') )
        if contador == 0:
            break
print('!!!FIM!!!')