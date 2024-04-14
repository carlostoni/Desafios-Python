#Crie um jogo da forca onde o jogador precisa adivinhar uma palavra secreta.

palavra = 'arvore' 
list = []
print('Voce esta parcipando de um jogo para adivinhar uma palavra\n')
print(f'Aqui esta a primeira dica a palavra tem {len(palavra)} letras')
i= 0

while i < 10:
    letra = input('Digite uma letra ')
    i+1

    if letra in palavra:
     posicao = palavra.find(letra)+1
     print(f'A letra {letra} esta na posicao {posicao}')
     list.append(letra)
     print(list)
     
     
    else:
     print('errado')
     

