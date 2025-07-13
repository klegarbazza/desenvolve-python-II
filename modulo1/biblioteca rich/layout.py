from rich.console import Console
from rich.panel import Panel

console = Console()

def imprimir_layout(texto: str, isArquivo: bool):
    """
    Imprime o texto em um painel.

    :param texto: Texto a ser impresso.
    :param isArquivo: Se True, considera texto como caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    panel = Panel(texto, title="Layout Panel")
    console.print(panel)

def imprimir_titulo(texto: str, isArquivo: bool):
    """
    Imprime o texto como título em um painel.

    :param texto: Texto a ser impresso.
    :param isArquivo: Se True, considera texto como caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    panel = Panel(texto, title="Título", style="bold red")
    console.print(panel)