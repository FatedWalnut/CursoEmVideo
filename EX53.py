frase = input('FRASE:').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('A FRASE É UM PALINDROMO')
else:
    print('A FRASE NÃO É UM PALINDROMO')