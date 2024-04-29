#Faça um programa de um caixa eletrônico que, a partir do valor a ser sacado informado pelo usuário, o programa informe a menor quantidade de cédulas que o usuário irá receber, 
#informando-o quantas cédulas e de quais valores ele irá receber.
#Considerar apenas notas:
# R$200,00
# R$100,00
# R$50,00
# R$20,00
# R$10,00
# R$5,00
# R$2,00
# R$1,00

# Exemplo:

# R$ 858,00

# O programa irá informar:
# Cédulas de 200 reais: 4
# Cédulas de 50 reais: 1
# Cédulas de 5 reais: 1
# Cédulas de 2 reais: 1
# Cédulas de 1 real: 1

cedulas200 = [200, 200, 200, 200]
cedulas50 = [50]
cedulas5 = [5]
cedulas2 = [2]
cedulas1 = [1]

soma = sum(cedulas200 + cedulas50 + cedulas5 + cedulas2 + cedulas1)

print("Soma das cédulas:", soma)

print(f'''Essas notas estao disponiveis 
      R$ 200: {cedulas200} notas
      R$ 50: {cedulas50} notas
      R$ 5: {cedulas5} notas
      R$ 2: {cedulas2} notas
      R$ 1: {cedulas1} notas''')

saque= int(input("Digite o valor que voçe deseja sacar: "))
