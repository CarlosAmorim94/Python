"""
EXERCÍCIO 037: Conversor de Bases Numéricas
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""

# Escolha do número:
num = int(input('Digite um número para a conversão: '))

# Escolha do método:
print('''Escolha uma das bases de conversão:
Digite [1] para BINÁRIO
Digite [2] para OCTAL
Digite [3] para HEXADECIMAL''')
cod = int(input('A conversão escolhida foi: '))

# Conversões:
if cod == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))

elif cod == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))

elif cod == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))

else:
    print('Opção inválida, tente novamente...')