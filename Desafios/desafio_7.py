#Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
#Aprovado  Acima de 7
#Reprovado  Abaixo de 5
#Recuperação  Entre 5 e 7

notas = []

print("insira a primeira nota")
notas.append(int(input()))

print("insira a segunda nota")
notas.append(int(input()))

media = (notas[0] + notas[1]) / 2 
print(media)
if media >= 7:
    print("Aprovado")
elif media >=5:
    print("Recuperacao")
else:
    print("Reprovado")