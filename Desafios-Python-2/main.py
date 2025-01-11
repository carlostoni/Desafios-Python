from estudante import Estudante  # Importa a classe Estudante
from curso import Curso          # Importa a classe Curso

# Criando estudantes
alunos = []

# Solicita a quantidade de alunos
quantidade = int(input("Digite o número de alunos: "))

# Loop para capturar os dados de cada aluno
for i in range(quantidade):
    print(f"\nDigite os dados do aluno {i + 1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    matricula = input("Matrícula: ")
    
    # Adiciona os dados do aluno como uma sublista na lista principal
    alunos.append([nome, idade, matricula])

# Criando um curso
curso = Curso("Matemática", "C001")

# Adicionando estudantes ao curso
curso.adicionar_estudante(alunos)


# Listando os estudantes do curso
curso.listar_estudantes()

# Exibindo detalhes de um estudante individual
print("\nDetalhes do estudante:")
print(alunos)
