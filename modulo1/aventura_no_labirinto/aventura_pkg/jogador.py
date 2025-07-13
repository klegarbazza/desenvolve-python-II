from pynput import keyboard

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.posicao = (0, 0)  # Posição inicial

    def mover(self, labirinto):
        """
        Move o jogador com base na tecla pressionada.

        :param labirinto: Labirinto onde o jogador se move.
        """
        def on_press(key):
            try:
                if key.char == 'w':  # Cima
                    self._atualizar_posicao(-1, 0, labirinto)
                elif key.char == 's':  # Baixo
                    self._atualizar_posicao(1, 0, labirinto)
                elif key.char == 'a':  # Esquerda
                    self._atualizar_posicao(0, -1, labirinto)
                elif key.char == 'd':  # Direita
                    self._atualizar_posicao(0, 1, labirinto)
            except AttributeError:
                pass

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def _atualizar_posicao(self, delta_x, delta_y, labirinto):
        """
        Atualiza a posição do jogador.

        :param delta_x: Mudança na coordenada x.
        :param delta_y: Mudança na coordenada y.
        :param labirinto: Labirinto onde o jogador se move.
        """
        nova_x = self.posicao[0] + delta_x
        nova_y = self.posicao[1] + delta_y
        if 0 <= nova_x < len(labirinto) and 0 <= nova_y < len(labirinto[0]) and labirinto[nova_x][nova_y] != '#':
            self.posicao = (nova_x, nova_y)
            self.pontuacao += 1  # Aumenta a pontuação ao mover
            print(f"Movido para {self.posicao}, Pontuação: {self.pontuacao}")

    def pontuar(self):
        """
        Retorna a pontuação atual do jogador.
        """
        return self.pontuacao
