import pygame

class GlavnoeMenu():
    def __init__(self, screen):
        self.screen = screen

    def risovanie(self, pic):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        pygame.draw.rect(self.screen, ('#808080'), (300, 225, 200, 65))
        pygame.draw.rect(self.screen, ('#808080'), (300, 310, 200, 65))
        pygame.draw.rect(self.screen, ('#808080'), (300, 395, 200, 65))
        pygame.draw.rect(self.screen, ('#808080'), (300, 480, 200, 65))
        q = pygame.font.SysFont('arial', 25)
        txt = q.render('Новая игра', True, (255, 255, 255))
        self.screen.blit(txt, (345, 245))
        txt = q.render('Настройки', True, (255, 255, 255))
        self.screen.blit(txt, (345, 330))
        txt = q.render('Управление', True, (255, 255, 255))
        self.screen.blit(txt, (345, 415))
        txt = q.render('Выход', True, (255, 255, 255))
        self.screen.blit(txt, (365, 500))
        return list([[300, 225, 300 + 200, 225 + 65], [300, 310, 300 + 200, 310 + 65],
                     [300, 395, 300 + 200, 395 + 65], [300, 480, 500, 545]])

    def type(self):
        return 'GlavnoeMenu'