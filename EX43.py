peso = float(input('SEU PESO ?'))
altura = float(input('SUA ALTURA?'))
IMC = peso/(altura**2)
if IMC <= 18.5 :
    print('ABAIXO DO PESO')
elif IMC > 18.5 and IMC <= 25:
    print('PESO IDEAL')
elif IMC > 25 and IMC <=30:
    print('SOBREPESO')
elif IMC >30 and IMC <= 40:
    print('OBESO')
elif IMC > 40:
    print('OBESO MORBIDO')