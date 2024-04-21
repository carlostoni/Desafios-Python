import random
class Jogo:
    def __init__(self):
        self.personagem_1 = [1, 2, 3]
        self.personagem_2 = [2, 1, 3]
        self.personagem_3 = [2, 3, 2]
    
    def oponente(self):
        self.oponente_1 = [1, 2, 3]
        self.oponente_2 = [2, 1, 3]
        self.oponente_3 = [3, 2, 1]
        
class Regra:
    def __init__(self):
        self.jogo = Jogo()
        self.jogo.oponente()
        
    def selecionar_personagem(self):
        print('''Selecione um personagem
              1 = Guerreiro
              2 = Mago
              3 = Druida''')
        self.selecao = int(input())
        
        if self.selecao == 1:
            self.personagem = self.jogo.personagem_1
            self.nome = "Guerreiro"
            
        elif self.selecao == 2:
            self.personagem = self.jogo.personagem_2
            self.nome = "Mago"
            
        elif self.selecao == 3:
            self.personagem = self.jogo.personagem_3
            self.nome = "Druida"
            
        else:
            print("Opcao invalida")
            
    def selecionar_oponente(self):
        self.lista_escolhida = random.choice([self.jogo.oponente_1, self.jogo.oponente_2, self.jogo.oponente_3])
        if self.lista_escolhida == self.jogo.oponente_1:
            self.nome_op = "Vampiro"
        elif self.lista_escolhida == self.jogo.oponente_2:
            self.nome_op = "Goblin"
        else:
            self.nome_op = "Gargula"
    def mostrar_informacoes(self):
        ataque, magia, vida = self.personagem
        ataque_op, magia_op, vida_op = self.lista_escolhida
        print(f"{self.nome} - Ataque: {ataque}, Magia: {magia}, Vida: {vida}")
        print(f"{self.nome_op} - Ataque: {ataque_op}, Magia: {magia_op}, Vida: {vida_op}") 

class Batalha:
    def __init__(self):
       print("Que comece a batalha")
       
regra = Regra()
regra.selecionar_personagem()
regra.selecionar_oponente()
regra.mostrar_informacoes()

batalha = Batalha()