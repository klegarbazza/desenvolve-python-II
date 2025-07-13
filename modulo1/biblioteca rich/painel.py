from rich.console import Console
from rich.panel import Panel

console = Console()

def imprimir_painel(texto: str, isArquivo: bool):
    """
    Imprime o texto em um painel.

    :param texto: Texto a ser impresso.
    :param isArquivo: Se True, considera texto como caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    panel = Panel(texto, title="Painel", border_style="blue")
    console.print(panel)

def imprimir_painel_destaque(texto: str, isArquivo: bool):
    """
    Imprime o texto em um painel destacado.

    :param texto: Texto a ser impresso.
    :param isArquivo: Se True, considera texto como caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    panel = Panel(texto, title="Painel Destaque", border_style="yellow")
    console.print(panel)