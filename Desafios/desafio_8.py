#Uma ótica quer fazer um desconto diferenciado com base na idade do usuário em um modelo de óculos que custa R$200,00.
#O desconto será igual a idade do usuário, porém o desconto mínimo será 10% e o desconto máximo será de 80%.
#Faça um programa que pergunte a idade do usuário e então mostre o valor final do óculos e o desconto adquirido.

oculos = 200

print("Digite a sua idade para ver o seu desconto")
desconto = int(input())

descontototal = oculos * (desconto /100)
total = oculos - descontototal

if desconto <= 10:
    descontototal = oculos * (10 /100)
    total = oculos - descontototal
    print(total)
    
else:
    print(total)

