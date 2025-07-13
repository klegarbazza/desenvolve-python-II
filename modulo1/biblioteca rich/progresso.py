from rich.console import Console
from rich.progress import Progress

console = Console()

def mostrar_progresso(texto: str, isArquivo: bool):
    """
    Mostra um progresso enquanto imprime o texto.

    :param texto: Texto a ser impresso.
    :param isArquivo: Se True, considera texto como caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Imprimindo texto...", total=len(texto))
        for char in texto:
            console.print(char, end='', flush=True)
            progress.update(task, advance=1)

def mostrar_progresso_arquivo(texto: str, isArquivo: bool):
    """
    Mostra um progresso ao imprimir o conteúdo de um arquivo.

    :param texto: Texto a ser impresso.
    :param isArquivo: Se True, considera texto como caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Imprimindo arquivo...", total=len(texto))
        for char in texto:
            console.print(char, end='', flush=True)
            progress.update(task, advance=1)