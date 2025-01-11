from estudante import Estudante  # Importa a classe Estudante

class Curso:
    def __init__(self, nome_curso, codigo_curso):
        """
        Inicializa um objeto Curso com nome, código e uma lista vazia de estudantes.
        """
        self.nome_curso = nome_curso
        self.codigo_curso = codigo_curso
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        """
        Adiciona um estudante à lista de estudantes do curso.
        """
        if isinstance(estudante, Estudante):
            self.estudantes.append(estudante)
            print(f"Estudante {estudante.nome} adicionado ao curso {self.nome_curso}.")
        else:
            print("Erro: O objeto fornecido não é um estudante válido.")

    def listar_estudantes(self):
        """
        Lista todos os estudantes matriculados no curso.
        """
        if not self.estudantes:
            print(f"O curso {self.nome_curso} não tem estudantes matriculados.")
        else:
            print(f"Estudantes no curso {self.nome_curso}:")
            for estudante in self.estudantes:
                print(f"- Nome: {estudante.nome}, Matrícula: {estudante.matricula}")
