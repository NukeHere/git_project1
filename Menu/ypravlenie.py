import pygame
from glavnoemenu import GlavnoeMenu

class Ypravlenie(GlavnoeMenu):

    def risovanie(self, pic):
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        q = pygame.font.SysFont('arial', 25)
        pygame.draw.rect(self.screen, ('#808080'), (10, 535, 150, 50)) #кнопка назад
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50, 545))
        pygame.draw.rect(self.screen, ('#808080'), (20, 20, 250, 400))
        txt = q.render('Первый игрок', True, (255, 255, 255))
        self.screen.blit(txt, (50, 50))
        txt = q.render('Движение танка:', True, (255, 255, 255))
        self.screen.blit(txt, (50, 80))
        txt = q.render('Вперёд: W', True, (255, 255, 255))
        self.screen.blit(txt, (50, 110))
        txt = q.render('Назад: S', True, (255, 255, 255))
        self.screen.blit(txt, (50, 140))
        txt = q.render('Налево: A', True, (255, 255, 255))
        self.screen.blit(txt, (50, 170))
        txt = q.render('Направо: D', True, (255, 255, 255))
        self.screen.blit(txt, (50, 200))
        txt = q.render('Движение башни:', True, (255, 255, 255))
        self.screen.blit(txt, (50, 230))
        txt = q.render('Налево: F', True, (255, 255, 255))
        self.screen.blit(txt, (50, 260))
        txt = q.render('Направо: H', True, (255, 255, 255))
        self.screen.blit(txt, (50, 290))
        txt = q.render('Выстрел: G', True, (255, 255, 255))
        self.screen.blit(txt, (50, 320))
        pygame.draw.rect(self.screen, ('#808080'), (320, 20, 300, 400))
        txt = q.render('Второй игрок', True, (255, 255, 255))
        self.screen.blit(txt, (350, 50))
        txt = q.render('Движение танка:', True, (255, 255, 255))
        self.screen.blit(txt, (350, 80))
        txt = q.render('Вперёд: Стрелка вверх', True, (255, 255, 255))
        self.screen.blit(txt, (350, 110))
        txt = q.render('Назад: Стрелка вниз', True, (255, 255, 255))
        self.screen.blit(txt, (350, 140))
        txt = q.render('Налево: Стрелка на лево', True, (255, 255, 255))
        self.screen.blit(txt, (350, 170))
        txt = q.render('Направо: Стрелка на право', True, (255, 255, 255))
        self.screen.blit(txt, (350, 200))
        txt = q.render('Движение башни:', True, (255, 255, 255))
        self.screen.blit(txt, (350, 230))
        txt = q.render('Налево: J', True, (255, 255, 255))
        self.screen.blit(txt, (350, 260))
        txt = q.render('Направо: L', True, (255, 255, 255))
        self.screen.blit(txt, (350, 290))
        txt = q.render('Выстрел: K', True, (255, 255, 255))
        self.screen.blit(txt, (350, 320))

    def type(self):
        return 'Ypravlenie'