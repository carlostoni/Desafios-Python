
#Uma empresa pretende fazer um reajuste salarial para os funcionários e precisa da sua ajuda para criar um programa. Ficou definido os seguintes reajustes:
#Salário Abaixo de R$1.500,00  Aumento de 25%
#Salário Entre de R$1.500,00 e R$1.999,99  Aumento de 20%
#Salário Entre de R$2.000,00 e R$2.999,99  Aumento de 15%
#Salário Entre de R$3.000,00 e R$4.999,99  Aumento de 10%
#Salário Acima de R$5.000,00  Aumento de 5%

#Faça um programa que pergunte ao usuário qual seu Salário Atual e mostre ao usuário:
#O salário atual;
#A porcentagem do reajuste;
#O aumento em R$;
#O salário final após o reajuste.

#Opcao 1
salario = float(input("Digite o seu salario: "))
if salario <= 1500:
   aumento = salario * (25 / 100)
elif salario<= 1999.99:
    aumento = salario * (20 / 100)
elif salario<= 2999.99:
    aumento = salario * (15 / 100)
elif salario<= 4999.99:
    aumento = salario * (10 / 100)
else:
    aumento = salario * (5 / 100)
total = salario + aumento
print(f"O aumento vai ser de {aumento} com isso o seu salario vai para {total} ")


#opcao 2
salario = int(input("Digite o seu salario: "))
porcentagem = int(input("Digite a porcentagem do aumento: "))

minmax = min(max(porcentagem,5), 25)
minmaxsa = min(max(salario,))

aumento = salario * (minmax / 100)
total = salario + aumento

print("O salario final e:", total)
print("O aumento do salario é: ", total - salario)    