soma = 0
cont = 0

for c in range(1 , 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números e a soma é {}'.format(cont , soma))
