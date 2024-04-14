#Uma empresa de transporte público quer fazer um sistema automático para 
#identificar se o usuário terá gratuidade no transporte ou não. 
#Faça um programa que pergunte a idade do usuário, se ele tiver 65 anos ou mais 
#irá informar que ele tem gratuidade no transporte.

print(f"Digite sua idade para ver se e legivel para gratuidade:")
idade = int(input())

if idade >= 65:
    print("Voce e legivel para gratuidade no transporte")
else:
    print("Voce nao e legivel para gratuidade no transporte")
    
    