import pygame
import constantes
import sprites
import os

class Game:
    def __init__(self):
        # Criando a tela do jogo
        pygame.init()
        pygame.mixer.init()

        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.isrunning = True
    

    def novo_jogo(self):
        # Instancia as classes das Sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()

        self.rodar()
    

    def rodar(self):
        # Loop do Jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()


    def eventos(self):
        # Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.isrunning = False



    def atualizar_sprites(self):
        # Atualizar Sprites
        self.todas_as_sprites.update()


    def desenhar_sprites(self):
        # Desenhar Sprites
        self.tela.fill(constantes.BLACK)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()
    

    def carregar_arquivos(self):
        # Carregar os arquivos do jogo
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')

    

    def mostrar_tela_start(self):...


    def mostrar_tela_game_over(self):...


g = Game()
g.mostrar_tela_start()

while g.isrunning:
    g.novo_jogo()
    g.mostrar_tela_game_over()
