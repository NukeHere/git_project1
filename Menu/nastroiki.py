import pygame
from glavnoemenu import GlavnoeMenu

class Nastroiki(GlavnoeMenu):
    def risovanie(self):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        q = pygame.font.SysFont('arial', 25)
        pygame.draw.rect(self.screen, ('#808080'), (10, 535, 150, 50))
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50, 545))
        return list([0, 1])

    def type(self):
        return 'Nastroiki'