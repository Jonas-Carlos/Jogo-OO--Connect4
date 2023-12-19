# main.py
import pygame
import sys
from model import *
from view import *
from controller import *
from constants import *

pygame.init()

def main():
    tabuleiro = [[0] * COLUNAS for _ in range(LINHAS)]
    screen = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Connect 4")

    jogador1, jogador2 = obter_nomes_jogadores(screen)

    jogador_atual = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coluna = event.pos[0] // TAMANHO_CELULA
                if fazer_movimento(tabuleiro, coluna, jogador_atual):
                    if verificar_vencedor(tabuleiro):
                        mensagem = f"{jogador_atual == 1 and jogador1 or jogador2} venceu!"
                        exibir_mensagem(screen, mensagem, PRETO)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        pygame.quit()
                        sys.exit()
                    jogador_atual = 3 - jogador_atual

        screen.fill(BRANCO)
        desenhar_tabuleiro(screen)
        desenhar_pecas(screen, tabuleiro)

        mensagem_vez = f"Vez do jogador: {jogador_atual == 1 and jogador1 or jogador2}"
        exibir_mensagem(screen, mensagem_vez, PRETO, tamanho=24)

        pygame.display.flip()

if __name__ == "__main__":
    main()
