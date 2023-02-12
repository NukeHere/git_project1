import pygame
from glavnoemenu import GlavnoeMenu

class Ypravlenie(GlavnoeMenu):

    def risovanie(self, pic):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        q = pygame.font.SysFont('arial', int(25 * self.screen_resolution))
        pygame.draw.rect(self.screen, ('#808080'), (10 * self.screen_resolution, 535 * self.screen_resolution,
                                                    150 * self.screen_resolution, 50 * self.screen_resolution)) #кнопка назад
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 545 * self.screen_resolution))
        pygame.draw.rect(self.screen, ('#808080'), (20 * self.screen_resolution, 20 * self.screen_resolution,
                                                    250 * self.screen_resolution, 400 * self.screen_resolution))
        txt = q.render('Первый игрок', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 50 * self.screen_resolution))
        txt = q.render('Движение танка:', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 80 * self.screen_resolution))
        txt = q.render('Вперёд: W', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 110 * self.screen_resolution))
        txt = q.render('Назад: S', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 140 * self.screen_resolution))
        txt = q.render('Налево: A', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 170 * self.screen_resolution))
        txt = q.render('Направо: D', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 200 * self.screen_resolution))
        txt = q.render('Движение башни:', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 230 * self.screen_resolution))
        txt = q.render('Налево: F', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 260 * self.screen_resolution))
        txt = q.render('Направо: H', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 290 * self.screen_resolution))
        txt = q.render('Выстрел: G', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 320 * self.screen_resolution))
        pygame.draw.rect(self.screen, ('#808080'), (320 * self.screen_resolution, 20 * self.screen_resolution,
                                                    300 * self.screen_resolution, 400 * self.screen_resolution))
        txt = q.render('Второй игрок', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 50 * self.screen_resolution))
        txt = q.render('Движение танка:', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 80 * self.screen_resolution))
        txt = q.render('Вперёд: Стрелка вверх', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 110 * self.screen_resolution))
        txt = q.render('Назад: Стрелка вниз', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 140 * self.screen_resolution))
        txt = q.render('Налево: Стрелка на лево', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 170 * self.screen_resolution))
        txt = q.render('Направо: Стрелка на право', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 200 * self.screen_resolution))
        txt = q.render('Движение башни:', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 230 * self.screen_resolution))
        txt = q.render('Налево: J', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 260 * self.screen_resolution))
        txt = q.render('Направо: L', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 290 * self.screen_resolution))
        txt = q.render('Выстрел: K', True, (255, 255, 255))
        self.screen.blit(txt, (350 * self.screen_resolution, 320 * self.screen_resolution))

    def type(self):
        return 'Ypravlenie'