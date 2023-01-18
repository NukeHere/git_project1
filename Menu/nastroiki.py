import pygame
from glavnoemenu import GlavnoeMenu

class Nastroiki(GlavnoeMenu):
    def risovanie(self, pic):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        q = pygame.font.SysFont('arial', 25)
        pygame.draw.rect(self.screen, ('#808080'), (10, 535, 150, 50))
        pygame.draw.rect(self.screen, ('#808080'), (200, 535, 150, 50))
        pygame.draw.rect(self.screen, ('#808080'), (10, 100, 150, 50))
        pygame.draw.rect(self.screen, ('#808080'), (10, 175, 150, 50))
        pygame.draw.rect(self.screen, ('#808080'), (10, 250, 150, 50))
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50, 545))
        txt = q.render('Разрешение', True, (255, 255, 255))
        self.screen.blit(txt, (20, 115))
        txt = q.render('Музыка', True, (255, 255, 255))
        self.screen.blit(txt, (40, 190))
        txt = q.render('Звуки', True, (255, 255, 255))
        self.screen.blit(txt, (55, 265))
        return list([[200, 535, 350, 585], [0, 1]])

    def type(self):
        return 'Nastroiki'