import pygame
from glavnoemenu import GlavnoeMenu

class Vibor(GlavnoeMenu):
    def risovanie(self, pic):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        pygame.draw.rect(self.screen, ('#808080'), (300 * self.screen_resolution, 225 * self.screen_resolution,
                                                    200 * self.screen_resolution, 65 * self.screen_resolution))
        pygame.draw.rect(self.screen, ('#808080'), (300 * self.screen_resolution, 310 * self.screen_resolution,
                                                    200 * self.screen_resolution, 65 * self.screen_resolution))
        pygame.draw.rect(self.screen, ('#808080'), (10 * self.screen_resolution, 535 * self.screen_resolution,
                                                    150 * self.screen_resolution, 50 * self.screen_resolution))
        q = pygame.font.SysFont('arial', int(25 * self.screen_resolution))
        txt = q.render('PvE 1x1', True, (255, 255, 255))
        self.screen.blit(txt, (365 * self.screen_resolution, 245 * self.screen_resolution))
        txt = q.render('PvE 2x2', True, (255, 255, 255)) # с PvP плохо усё
        self.screen.blit(txt, (365 * self.screen_resolution, 330 * self.screen_resolution))
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 545 * self.screen_resolution))
        return list([[300 * self.screen_resolution, 225 * self.screen_resolution,
                      500 * self.screen_resolution, 290 * self.screen_resolution],
                     [300 * self.screen_resolution, 310 * self.screen_resolution,
                      500 * self.screen_resolution, 375 * self.screen_resolution]])

    def type(self):
        return 'Vibor'