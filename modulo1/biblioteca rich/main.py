import argparse
from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(description="Imprimir texto formatado com Rich.")
    parser.add_argument("texto", help="Texto ou caminho para um arquivo a ser impresso.")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um caminho para um arquivo.")
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"], required=True, help="Módulo a ser acessado.")
    parser.add_argument("-f", "--funcao", choices=["imprimir_layout", "imprimir_titulo", "imprimir_painel", "imprimir_painel_destaque", "mostrar_progresso", "mostrar_progresso_arquivo", "imprimir_texto_estilizado", "imprimir_texto_substituto"], required=True, help="Função a ser acessada.")

    args = parser.parse_args()

    if args.modulo == "layout":
        if args.funcao == "imprimir_layout":
            layout.imprimir_layout(args.texto, args.arquivo)
        elif args.funcao == "imprimir_titulo":
            layout.imprimir_titulo(args.texto, args.arquivo)
    elif args.modulo == "painel":
        if args.funcao == "imprimir_painel":
            painel.imprimir_painel(args.texto, args.arquivo)
        elif args.funcao == "imprimir_painel_destaque":
            painel.imprimir_painel_destaque(args.texto, args.arquivo)
    elif args.modulo == "progresso":
        if args.funcao == "mostrar_progresso":
            progresso.mostrar_progresso(args.texto, args.arquivo)
        elif args.funcao == "mostrar_progresso_arquivo":
            progresso.mostrar_progresso_arquivo(args.texto, args.arquivo)
    elif args.modulo == "estilo":
        if args.funcao == "imprimir_texto_estilizado":
            estilo.imprimir_texto_estilizado(args.texto, args.arquivo)
        elif args.funcao == "imprimir_texto_substituto":
            estilo.imprimir_texto_substituto(args.texto, args.arquivo)

if __name__ == "__main__":
    main()