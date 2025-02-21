alunos = {}

numero_de_alunos = int(input('Digite a quantidade de alunos: '))

for i in range(numero_de_alunos):
    nome_aluno = input('Digite o nome do aluno: ')
    nota = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    alunos[nome_aluno] = [nota, nota2]

    for nome, numeros in alunos.items():
        soma = sum(alunos[nome][:2])
        print(f"{nome} {soma/2}")
