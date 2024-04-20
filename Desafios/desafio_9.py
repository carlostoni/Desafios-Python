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
        self.jogo.oponente()
        
    def selecionar_personagem(self):
        print('''Selecione um personagem
              1 = Guerreiro
              2 = Mago''')
        
        self.selecao = int(input())
        if self.selecao == 1:
            self.personagem = self.jogo.personagem_1
            self.nome = "Guerreiro"
            
        elif self.selecao == 2:
            self.personagem = self.jogo.personagem_2
            self.nome = "Mago"
            
        else:
            print("Opcao invalida")
            
    def selecionar_oponente(self):
        self.lista_escolhida = random.choice([self.jogo.oponente_1, self.jogo.oponente_2])
        if self.lista_escolhida == self.jogo.oponente_1:
            self.nome_op = "Vampiro"
        else:
            self.nome_op = "Gargula"
        

# Exemplo de uso:
regra = Regra()
regra.selecionar_personagem()
regra.selecionar_oponente()

print(f"{regra.nome} {regra.personagem}")  
print(f"{regra.nome_op} {regra.lista_escolhida}")