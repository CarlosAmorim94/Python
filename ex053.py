frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(frase, inverso ))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')