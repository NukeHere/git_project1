import pygame


class GlavnoeMenu():
    def __init__(self, screen, screen_resolution):
        self.screen = screen
        self.screen_resolution = screen_resolution

    def risovanie(self, pic):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        pygame.draw.rect(self.screen, ('#808080'), (300 * self.screen_resolution,
                                                    225 * self.screen_resolution, 200 * self.screen_resolution,
                                                    65 * self.screen_resolution))# кнопка новая игра
        pygame.draw.rect(self.screen, ('#808080'), (300 * self.screen_resolution,
                                                    310 * self.screen_resolution, 200 * self.screen_resolution,
                                                    65 * self.screen_resolution))# кнопка настройки
        pygame.draw.rect(self.screen, ('#808080'), (300 * self.screen_resolution,
                                                    395 * self.screen_resolution, 200 * self.screen_resolution,
                                                    65 * self.screen_resolution))# кнопка управление
        pygame.draw.rect(self.screen, ('#808080'), (300 * self.screen_resolution,
                                                    480 * self.screen_resolution, 200 * self.screen_resolution,
                                                    65 * self.screen_resolution))# кнопка выход
        q = pygame.font.SysFont('arial', int(25 * self.screen_resolution))
        txt = q.render('Новая игра', True, (255, 255, 255))
        self.screen.blit(txt, (345 * self.screen_resolution,
                               245 * self.screen_resolution))
        txt = q.render('Настройки', True, (255, 255, 255))
        self.screen.blit(txt, (345 * self.screen_resolution,
                               330 * self.screen_resolution))
        txt = q.render('Управление', True, (255, 255, 255))
        self.screen.blit(txt, (345 * self.screen_resolution,
                               415 * self.screen_resolution))
        txt = q.render('Выход', True, (255, 255, 255))
        self.screen.blit(txt, (365 * self.screen_resolution,
                               500 * self.screen_resolution))
        return list([[300 * self.screen_resolution, 225 * self.screen_resolution,
                      300 * self.screen_resolution + 200 * self.screen_resolution,
                      225 * self.screen_resolution + 65 * self.screen_resolution],
                     [300 * self.screen_resolution, 310 * self.screen_resolution,
                      300 * self.screen_resolution + 200 * self.screen_resolution,
                      310 * self.screen_resolution + 65 * self.screen_resolution],
                     [300 * self.screen_resolution, 395 * self.screen_resolution,
                      300 * self.screen_resolution + 200 * self.screen_resolution,
                      395 * self.screen_resolution + 65 * self.screen_resolution],
                     [300 * self.screen_resolution, 480 * self.screen_resolution,
                      300 * self.screen_resolution + 200 * self.screen_resolution,
                      480 * self.screen_resolution + 65 * self.screen_resolution]])

    def type(self):
        return 'GlavnoeMenu'
