from rich.console import Console

console = Console()

def imprime_instrucoes():
    """
    Lê e imprime as instruções do jogo.
    """
    instrucoes = """
    Bem-vindo à Aventura no Labirinto!
    Use 'w' para mover para cima, 's' para baixo, 'a' para esquerda e 'd' para direita.
    O objetivo é chegar ao final do labirinto (E) a partir do ponto de partida (S).
    """
    console.print(instrucoes)

def imprime_menu():
    """
    Imprime o menu principal do jogo.
    """
    console.print("1. Instruções")
    console.print("2. Jogar")
    console.print("3. Sair")
