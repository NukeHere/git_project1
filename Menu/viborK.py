import pygame
from glavnoemenu import GlavnoeMenu


class vibor_kart(GlavnoeMenu):
    def risovanie(self, pic):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        pygame.draw.rect(self.screen, ('#808080'), (300, 225, 200, 65))
        pygame.draw.rect(self.screen, ('#808080'), (300, 310, 200, 65))
        pygame.draw.rect(self.screen, ('#808080'), (10, 535, 150, 50))
        pygame.draw.rect(self.screen, ('#808080'), (300, 395, 200, 65))
        q = pygame.font.SysFont('arial', 25)
        txt = q.render('Лес', True, (255, 255, 255))
        self.screen.blit(txt, (365, 245))
        txt = q.render('Болото', True, (255, 255, 255))
        self.screen.blit(txt, (365, 330))
        txt = q.render('Пустыня', True, (255, 255, 255))
        self.screen.blit(txt, (365, 415))
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50, 545))
        return list([[300, 225, 300 + 200, 225 + 65], [300, 310, 300 + 200, 310 + 65],
                     [300, 395, 300 + 200, 395 + 65]])
    
    def type(self):
        return 'Vibor Kart'