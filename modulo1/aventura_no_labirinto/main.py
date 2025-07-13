import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import Jogador
from aventura_pkg.utils import imprime_instrucoes, imprime_menu

def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--color", help="Cor principal do jogo")
    parser.add_argument("--dificuldade", type=int, choices=[5, 10], default=5, help="Dificuldade do labirinto")
    parser.add_argument("--disable-sound", action="store_true", help="Desabilitar som")
    
    args = parser.parse_args()

    jogador = Jogador(args.name)
    
    while True:
        imprime_menu()
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case "1":
                imprime_instrucoes()
            case "2":
                labirinto = criar_labirinto(args.dificuldade)
                imprimir_labirinto(labirinto)
                jogador.mover(labirinto)
            case "3":
                print("Saindo do jogo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
