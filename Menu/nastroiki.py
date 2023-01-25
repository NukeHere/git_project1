import pygame
from glavnoemenu import GlavnoeMenu


SCREEN_RESOLATION = 1
VOLUEME_Z = 1
VOLUEME_M = 1
SCREEN_RESOLATION_LIST = ['800x600', '960x720', 0]
F = False

class Nastroiki(GlavnoeMenu):
    def risovanie2(self):
        pygame.font.init()
        q = pygame.font.SysFont('arial', 25)
        pygame.draw.rect(self.screen, ('#FFFFFF'), (185, 150, 150, 50))
        pygame.draw.rect(self.screen, ('#FFFFFF'), (185, 200, 150, 50))
        txt = q.render(f'{SCREEN_RESOLATION_LIST[0]}', True, (0, 0, 0))
        self.screen.blit(txt, (225, 160))
        txt = q.render(f'{SCREEN_RESOLATION_LIST[1]}', True, (0, 0, 0))
        self.screen.blit(txt, (225, 210))
    def risovanie(self, pic):
        global SCREEN_RESOLATION_LIST, F
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        q = pygame.font.SysFont('arial', 25)
        pygame.draw.rect(self.screen, ('#808080'), (10, 535, 150, 50)) #кнопка назад

        pygame.draw.rect(self.screen, ('#808080'), (10, 100, 150, 50)) #кнопка изменения разрешения
        pygame.draw.rect(self.screen, ('#FFFFFF'), (185, 100, 150, 50))

        pygame.draw.rect(self.screen, ('#808080'), (400, 100, 150, 50))
        pygame.draw.rect(self.screen, ('#808080'), (400, 175, 150, 50))
        pygame.draw.rect(self.screen, ('#FFFFFF'), (575, 100, 85, 50)) #вывод процентов громкости музыки
        pygame.draw.rect(self.screen, ('#FFFFFF'), (575, 175, 85, 50)) #вывод процентов громкости звуков

        pygame.draw.rect(self.screen, ('#808080'), (740, 100, 50, 50)) #кнопки изменения громкости музыки
        pygame.draw.rect(self.screen, ('#808080'), (675, 100, 50, 50))
        pygame.draw.line(self.screen, ('#FFFFFF'), (700, 110), (700, 140), 5)
        pygame.draw.line(self.screen, ('#FFFFFF'), (685, 125), (715, 125), 5)
        pygame.draw.line(self.screen, ('#FFFFFF'), (750, 125), (780, 125), 5)

        pygame.draw.rect(self.screen, ('#808080'), (675, 175, 50, 50)) #кнопки изменения громкости звуков
        pygame.draw.rect(self.screen, ('#808080'), (740, 175, 50, 50))
        pygame.draw.line(self.screen, ('#FFFFFF'), (700, 185), (700, 215), 5)
        pygame.draw.line(self.screen, ('#FFFFFF'), (685, 200), (715, 200), 5)
        pygame.draw.line(self.screen, ('#FFFFFF'), (750, 200), (780, 200), 5)
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50, 545))
        txt = q.render('Разрешение', True, (255, 255, 255))
        self.screen.blit(txt, (20, 115))
        txt = q.render('Музыка', True, (255, 255, 255))
        self.screen.blit(txt, (440, 110))
        txt = q.render('Звуки', True, (255, 255, 255))
        self.screen.blit(txt, (445, 190))
        txt = q.render(f'{int(round(VOLUEME_M * 100,0))}%', True, (0, 0, 0))
        self.screen.blit(txt, (590, 110))
        txt = q.render(f'{int(round(VOLUEME_Z * 100, 0))}%', True, (0, 0, 0))
        self.screen.blit(txt, (590, 185))
        txt = q.render(f'{SCREEN_RESOLATION_LIST[SCREEN_RESOLATION_LIST[-1]]}', True, (0, 0, 0))
        self.screen.blit(txt, (225, 110))
        if (F):
            risovanie2()
        return list([[740, 100, 790, 150], [675, 100, 735, 150], [675, 175, 725, 225], [740, 175, 790, 225],
                     [185, 100, 185 + 150, 150]])

    def type(self):
        return 'Nastroiki'

    def plusORminusZvuki(self, q, w):
        global VOLUEME_M, VOLUEME_Z
        if (w == 0):
            if (q == 0 and VOLUEME_M < 1):
                VOLUEME_M = VOLUEME_M + 0.05
                VOLUEME_M = round(VOLUEME_M, 2)
            elif (q == 1 and VOLUEME_M > 0):
                VOLUEME_M = VOLUEME_M - 0.05
                VOLUEME_M = round(VOLUEME_M, 2)
        else:
            if (q == 0 and VOLUEME_Z < 1):
                VOLUEME_Z = VOLUEME_Z + 0.05
                VOLUEME_Z = round(VOLUEME_Z, 2)
                return VOLUEME_Z
            elif (q == 1 and VOLUEME_Z > 0):
                VOLUEME_Z = VOLUEME_Z - 0.05
                VOLUEME_Z = round(VOLUEME_Z, 2)
                return VOLUEME_Z

    def new_resolution(self, q):
        global SCREEN_RESOLATION, SCREEN_RESOLATION_LIST
        if (q == 0):
            SCREEN_RESOLATION_LIST[-1] = 0
            SCREEN_RESOLATION = 1
        elif (q == 1):
            SCREEN_RESOLATION_LIST[-1] = 1
            SCREEN_RESOLATION = 1.2

