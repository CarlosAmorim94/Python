"""
EXERCÍCIO 008: Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

m = float(input('Digite um valor em metros: '))
print('O valor de {}M em centímetros é de {}cm \n O valor de {}M em milímetros é de {}mm'.format(m,(m*100),m,(m*1000)))