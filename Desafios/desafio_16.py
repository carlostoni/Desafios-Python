#Faça um jogo de Pedra, Papel e Tesoura.
#No qual você digitará a letra P para jogar Papel, a letra R para jogar Pedra e a letra T para jogar Tesoura.
#Você jogará contra o computador e contabilizara o número de vitórias, empates e derrotas.

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

entrada = input("Insira ")

if entrada == pedra: 
    if pedra > tesoura:
        print("venceu")
    elif pedra < papel:
        print("perdeu")