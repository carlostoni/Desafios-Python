#Faça um jogo de Pedra, Papel e Tesoura.
#No qual você digitará a letra P para jogar Papel, a letra R para jogar Pedra e a letra T para jogar Tesoura.
#Você jogará contra o computador e contabilizara o número de vitórias, empates e derrotas.

import random

list = ['pedra', 'papel', 'tesoura']

ranlist = random.choice(list)
print(ranlist)

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

entrada = input("Insira ")

if entrada == pedra: 
    if ranlist == "tesoura":
        if pedra > tesoura:
         print("venceu")
        else:
            print("perdeu")

cpf = []
email = []
compra = []

produtos_frutas = ['maça', 'banana', 'laranja', 'pera']
produtos_bebidas = ['cha', 'agua', 'coca-cola', 'energetico']

print('--- iniciar uma compra ---')
opcao = input('sim ou nao: ')

if opcao.lower() == 'sim':
    print('quais itens deseja:')
    for index, pro in enumerate(produtos_frutas):
        print(f'index frutas: {index} = {pro}')
    for index, pro in enumerate(produtos_bebidas):
        print(f'index bebidas: {index} = {pro}')

    opcao = input('vamos comecar pelas frutas, sim ou nao: ')
    if opcao.lower() == 'sim':
        while True:
            try:
                index_fruta = int(input('digite o índice do produto (ou -1 para parar): '))
                if index_fruta == -1:
                    break
                if 0 <= index_fruta < len(produtos_frutas):
                    compra.append(produtos_frutas[index_fruta])
                else:
                    print("Índice inválido. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")
    
    opcao = input('deseja adicionar bebidas, sim ou nao: ')
    if opcao.lower() == 'sim':
        while True:
            try:
                index_bebida = int(input('digite o índice do produto (ou -1 para parar): '))
                if index_bebida == -1:
                    break
                if 0 <= index_bebida < len(produtos_bebidas):
                    compra.append(produtos_bebidas[index_bebida])
                else:
                    print("Índice inválido. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

print(f'Produtos selecionados: {compra}')