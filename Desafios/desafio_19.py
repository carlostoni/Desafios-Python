def pode_colocar(matriz, linha, coluna, num):
    bloco_l, bloco_c = (linha // 3) * 3, (coluna // 3) * 3
    return not any(
        matriz[linha][i] == num or 
        matriz[i][coluna] == num or 
        matriz[bloco_l + i // 3][bloco_c + i % 3] == num 
        for i in range(9)
    )

def resolver_sudoku(matriz):
    for linha in range(9):
        for coluna in range(9):
            if matriz[linha][coluna] == 0:
                for num in range(1, 10):
                    if pode_colocar(matriz, linha, coluna, num):
                        matriz[linha][coluna] = num
                        if resolver_sudoku(matriz):
                            return True
                        matriz[linha][coluna] = 0
                return False
    return True

matriz = [[0] * 9 for _ in range(9)]

# Definição das posições iniciais de forma mais legível
posicoes = [
    (0, 0, 5), (0, 1, 3), (0, 4, 7),
    (1, 0, 6), (1, 3, 1), (1, 4, 9), (1, 5, 5),
    (2, 1, 9), (2, 2, 8), (2, 7, 6),
    (3, 0, 8), (3, 4, 6), (3, 8, 3),
    (4, 0, 4), (4, 3, 8), (4, 5, 3), (4, 8, 1),
    (5, 0, 7), (5, 4, 2), (5, 8, 6),
    (6, 1, 6), (6, 6, 2), (6, 7, 8),
    (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 8, 5),
    (8, 4, 8), (8, 7, 7), (8, 8, 9)
]

# Inserindo os valores na matriz
for linha, coluna, valor in posicoes:
    matriz[linha][coluna] = valor

# Resolver o Sudoku antes de imprimir
if resolver_sudoku(matriz):
    print("Sudoku resolvido com sucesso!")
else:
    print("Não foi possível resolver o Sudoku.")

# Exibindo a matriz resolvida
for linha in matriz:
    print(linha)
