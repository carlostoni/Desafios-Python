import random
class Jogo:
    def __init__(self):
        self.personagem_1 = [1, 2, 3]
        self.personagem_2 = [2, 1, 3]
    def oponente(self):
        self.oponente_1 = [1, 2, 3]
        self.oponente_2 = [2, 1, 3]
class Regra:
    def __init__(self):
        self.jogo = Jogo()

    def selecionar_personagem(self):
        print('''Selecione um personagem
              1 = Guerreiro
              2 = personagem_2''')
        self.selecao = int(input())
        if self.selecao == 1:
            personagem_1 = self.jogo.personagem_1
            self.nome = "Guerreiro"
            return personagem_1
        elif self.selecao == 2:
            personagem_2 = self.jogo.personagem_2
            self.nome = "Mago"
            return personagem_2
        else:
            print("Opcao invalida")
            
    def selecionar_oponente(self):
        self.jogo.oponente()
        self.lista_escolhida = random.choice([self.jogo.oponente_1, self.jogo.oponente_2])
        
        return self.lista_escolhida

# Exemplo de uso:
regra = Regra()
jogo = Jogo()
personagem_selecionado = regra.selecionar_personagem()
oponente_selecionado = regra.selecionar_oponente()
print(f"{regra.nome} {personagem_selecionado}")  
print(oponente_selecionado)