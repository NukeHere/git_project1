import pygame
from glavnoemenu import GlavnoeMenu

class Vibor(GlavnoeMenu):
    def risovanie(self):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, ('#808080'), (300, 225, 200, 65))
        pygame.draw.rect(self.screen, ('#808080'), (300, 310, 200, 65))
        pygame.draw.rect(self.screen, ('#808080'), (10, 535, 150, 50))
        q = pygame.font.SysFont('arial', 25)
        txt = q.render('PvP 1x1', True, (255, 255, 255))
        self.screen.blit(txt, (365, 245))
        txt = q.render('PvE', True, (255, 255, 255))
        self.screen.blit(txt, (380, 330))
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50, 545))
        return list([[300, 225, 300 + 200, 225 + 65], [300, 310, 300 + 200, 310 + 65]])

    def type(self):
        return 'Vibor'