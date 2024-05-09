#Faça um programa para avaliar qual o número que mais cai em um lance de dois dados (D6).
#O sistema deverá lançar um conjunto de dois dados n vezes seguidas, onde n é o número de vezes que você informar ao computador.
#Após jogar os dados, o sistema deverá informar quantas vezes a soma deu cada um dos números possíveis: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12.

import random

numero = int(input('Quantas vezes voce deseja lancar o dado: '))
numeros_in =[]
for i in range(numero):
    random_1 = random.randint(1, 6)

    random_2 = random.randint(1, 6)
    
    numeros_in.append(random_1)
    numeros_in.append(random_2)
    print(numeros_in)
    
pass