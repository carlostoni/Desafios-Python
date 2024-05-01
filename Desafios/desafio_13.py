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
cedulas100 = [100, 100]
cedulas50 = [50, 50]
cedulas20 = [20, 20]
cedulas10 = [10, 10]
cedulas5 = [5]
cedulas2 = [2]
cedulas1 = [1]

total_cedulas = len(cedulas200 + cedulas100 + cedulas50 + cedulas20 + cedulas10 + cedulas5 + cedulas2 + cedulas1)
soma = sum(cedulas200 + cedulas100 + cedulas50 + cedulas20 + cedulas10 + cedulas5 + cedulas2 + cedulas1)

#print("Total de cédulas na lista:", total_cedulas)
print(f'''Total de notas disponoveis sâo {total_cedulas}
Sendo {len(cedulas200)} de Notas R$200 
Sendo {+ len(cedulas100)} de Notas R$100 
Sendo {+ len(cedulas50)} de Notas R$50  
Sendo {+ len(cedulas20)} de Notas R$20 
Sendo {+ len(cedulas10)} de Notas R$10 
Sendo {+ len(cedulas5)} de Notas R$5  
Sendo {+ len(cedulas2)} de Notas R$2  
Sendo {+ len(cedulas1)} de Notas R$1 ''')

print("Soma das cédulas:", soma)


saque= int(input("Digite o valor que voçe deseja sacar: "))

if soma > saque:
    print(soma - saque)