from rich.console import Console
from rich.text import Text

console = Console()

def imprimir_texto_estilizado(texto: str, isArquivo: bool):
    """
    Imprime o texto com estilo.

    :param texto: Texto a ser impresso.
    :param isArquivo: Se True, considera texto como caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    styled_text = Text(texto, style="bold magenta")
    console.print(styled_text)

def imprimir_texto_substituto(texto: str, isArquivo: bool):
    """
    Imprime o texto com estilo substituto.

    :param texto: Texto a ser impresso.
    :param isArquivo: Se True, considera texto como caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    styled_text = Text(texto, style="italic green")
    console.print(styled_text)