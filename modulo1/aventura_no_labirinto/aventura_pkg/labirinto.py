import random
from rich.console import Console

console = Console()

def criar_labirinto(tamanho=5):
    """
    Cria um labirinto aleatório.

    :param tamanho: Tamanho do labirinto (número de células).
    :return: Labirinto como uma lista de listas.
    """
    labirinto = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
    for i in range(tamanho):
        for j in range(tamanho):
            if random.random() < 0.3:  # 30% de chance de ser uma parede
                labirinto[i][j] = '#'
    labirinto[0][0] = 'S'  # Ponto de partida
    labirinto[tamanho-1][tamanho-1] = 'E'  # Ponto de chegada
    return labirinto

def imprimir_labirinto(labirinto):
    """
    Imprime o labirinto no console.

    :param labirinto: Labirinto a ser impresso.
    """
    for linha in labirinto:
        console.print(' '.join(linha))
