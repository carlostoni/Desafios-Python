#Leia o texto abaixo sobre o Ano Bissexto:
# “O calendário gregoriano, estabelecido pela primeira vez em 1582 pelo Papa Gregório XIII, 
# foi projetado para corrigir os erros introduzidos pelo calendário juliano, que é menos preciso.

# No calendário gregoriano, um ano normal consiste em 365 dias. 
# Como o comprimento real de um ano sideral (o tempo necessário para a Terra girar uma vez sobre o Sol)
# é na verdade de 365,2425 dias, um "ano bissexto" de 366 dias é usado uma vez a cada quatro anos para eliminar o erro causado por três anos normais (mas curtos).
# Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto: por exemplo, 1988, 1992 e 1996 são anos bissextos.

# No entanto, ainda há um pequeno erro que deve ser contabilizado. Para eliminar esse erro, 
# o calendário gregoriano estipula que um ano que é uniformemente divisível por 100 (por exemplo, 1900) 
# é um ano bissexto apenas se também é igualmente divisível por 400.

# Por essa razão, os seguintes anos não são bissextos:
# 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600:
# Isso porque eles são uniformemente divisíveis por 100, mas não por 400.
# Os seguintes anos são bissextos: 1600, 2000, 2400
# Isso porque eles são uniformemente divisíveis por 100 e 400.”
# Faça um programa no qual o usuário informe um ano e o sistema responda se o ano é bissexto ou não.

ano = int(input("Informe ono desejado: "))
bissexto = ano % 4 == 0

if bissexto == True:
    print("e bissexto")
else:
    print("nao e bissexto", bissexto)