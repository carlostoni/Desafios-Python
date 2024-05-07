#Faça um programa para adivinhar um número de 0 a 10000.
#Se você errar o computador deverá responder se é mais ou menos.
#Se você errar 10 vezes você perde o jogo.

import random


numero = int(input('insira um numero entre 0 e 10000: '))

random_nu = random.randint(0, 10000)

if random_nu > 5000:
    print('maior')
    print(random_nu)
else:
    print('menor')
    print(random_nu)