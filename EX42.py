segmento1 = int(input('primeiro segmento'))
segmento2 = int(input('segundo segmento'))
segmento3 = int(input('terceiro segmento'))
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('COM ESSES SEGMENTOS È POSSIVEL FORMAR UM TRIÂNGULO')
    if segmento1 == segmento2 == segmento3:
        print('EQUILÁTERO, TODOS LADOS IGUAIS')
    elif segmento1 == segmento2 != segmento3 or segmento2 == segmento3 != segmento1 or segmento1 == segmento3 != segmento2:
        print('ISÓCELES, DOIS LADOS IGUAIS')
    elif segmento1 != segmento2 != segmento3:
        print('ESCALENO, TODOS OS LADOS DIFERENTES')
else:
    print('OS SEGMENTOS NÂO FORMAM UM TRIÂNGULO')