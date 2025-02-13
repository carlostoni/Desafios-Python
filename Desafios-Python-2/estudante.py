class Estudante:
    def __init__(self, nome, idade, matricula):
        """
        Inicializa um objeto Estudante com nome, idade e matrícula.
        """
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def exibir_detalhes(self):
        """
        Exibe os detalhes do estudante.
        """
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matrícula: {self.matricula}")
