import pygame
from glavnoemenu import GlavnoeMenu


class vibor_kart(GlavnoeMenu):
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
        pygame.draw.rect(self.screen, ('#808080'), (300 * self.screen_resolution, 395 * self.screen_resolution,
                                                    200 * self.screen_resolution, 65 * self.screen_resolution))
        q = pygame.font.SysFont('arial', int(25 * self.screen_resolution))
        txt = q.render('Лес', True, (255, 255, 255))
        self.screen.blit(txt, (365 * self.screen_resolution, 245 * self.screen_resolution))
        txt = q.render('Болото', True, (255, 255, 255))
        self.screen.blit(txt, (365 * self.screen_resolution, 330 * self.screen_resolution))
        txt = q.render('Пустыня', True, (255, 255, 255))
        self.screen.blit(txt, (365 * self.screen_resolution, 415 * self.screen_resolution))
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 545 * self.screen_resolution))
        return list([[300 * self.screen_resolution, 225 * self.screen_resolution,
                      500 * self.screen_resolution, 295 * self.screen_resolution],
                     [300 * self.screen_resolution, 310 * self.screen_resolution,
                      500 * self.screen_resolution, 375 * self.screen_resolution],
                     [300 * self.screen_resolution, 395 * self.screen_resolution,
                      500 * self.screen_resolution, 460 * self.screen_resolution]])

    def type(self):
        return 'Vibor Kart'