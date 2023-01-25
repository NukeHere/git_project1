import pygame
from glavnoemenu import GlavnoeMenu


SCREEN_RESOLATION = 1
VOLUEME_Z = 1
VOLUEME_M = 1
SCREEN_RESOLATION_LIST = ['800x600', '960x720', 0]

class Nastroiki(GlavnoeMenu):
    def risovanie(self, pic, f = False):
        global SCREEN_RESOLATION_LIST
        pygame.font.init()
        self.screen.fill((0, 0, 0))
        self.screen.blit(pic, (0, 0))
        q = pygame.font.SysFont('arial', 25)
        pygame.draw.rect(self.screen, ('#808080'), (10 * self.screen_resolution,
                                                    535 * self.screen_resolution, 150 * self.screen_resolution,
                                                    50 * self.screen_resolution)) #кнопка назад

        pygame.draw.rect(self.screen, ('#808080'), (10 * self.screen_resolution, 100 * self.screen_resolution,
                                                    150 * self.screen_resolution,
                                                    50 * self.screen_resolution)) #кнопка изменения разрешения
        pygame.draw.rect(self.screen, ('#FFFFFF'), (185 * self.screen_resolution, 100 * self.screen_resolution,
                                                    150 * self.screen_resolution, 50 * self.screen_resolution))

        pygame.draw.rect(self.screen, ('#808080'), (400 * self.screen_resolution, 100 * self.screen_resolution,
                                                    150 * self.screen_resolution, 50 * self.screen_resolution))
        pygame.draw.rect(self.screen, ('#808080'), (400 * self.screen_resolution, 175 * self.screen_resolution,
                                                    150 * self.screen_resolution, 50 * self.screen_resolution))
        pygame.draw.rect(self.screen, ('#FFFFFF'), (575 * self.screen_resolution, 100 * self.screen_resolution,
                                                    85 * self.screen_resolution, 50 * self.screen_resolution)) #вывод процентов громкости музыки
        pygame.draw.rect(self.screen, ('#FFFFFF'), (575 * self.screen_resolution, 175 * self.screen_resolution,
                                                    85 * self.screen_resolution, 50 * self.screen_resolution)) #вывод процентов громкости звуков

        pygame.draw.rect(self.screen, ('#808080'), (740 * self.screen_resolution, 100 * self.screen_resolution,
                                                    50 * self.screen_resolution, 50 * self.screen_resolution)) #кнопки изменения громкости музыки
        pygame.draw.rect(self.screen, ('#808080'), (675 * self.screen_resolution, 100 * self.screen_resolution,
                                                    50 * self.screen_resolution, 50 * self.screen_resolution))
        pygame.draw.line(self.screen, ('#FFFFFF'), (int(700 * self.screen_resolution), (int(110 * self.screen_resolution))),
                         (int(700 * self.screen_resolution), int(140 * self.screen_resolution)), int(5 * self.screen_resolution))
        pygame.draw.line(self.screen, ('#FFFFFF'), (int(685 * self.screen_resolution), int(125 * self.screen_resolution)),
                         (int(715 * self.screen_resolution), int(125 * self.screen_resolution)), int(5 * self.screen_resolution))
        pygame.draw.line(self.screen, ('#FFFFFF'), (int(750 * self.screen_resolution), int(125 * self.screen_resolution)),
                         (int(780 * self.screen_resolution), int(125 * self.screen_resolution)), int(5 * self.screen_resolution))

        pygame.draw.rect(self.screen, ('#808080'), (675 * self.screen_resolution, 175 * self.screen_resolution,
                                                    50 * self.screen_resolution, 50 * self.screen_resolution)) #кнопки изменения громкости звуков
        pygame.draw.rect(self.screen, ('#808080'), (740 * self.screen_resolution, 175 * self.screen_resolution,
                                                    50 * self.screen_resolution, 50 * self.screen_resolution))
        pygame.draw.line(self.screen, ('#FFFFFF'), (int(700 * self.screen_resolution), int(185 * self.screen_resolution)),
                         (int(700 * self.screen_resolution), int(215 * self.screen_resolution)), int(5 * self.screen_resolution))
        pygame.draw.line(self.screen, ('#FFFFFF'), (int(685 * self.screen_resolution), int(200 * self.screen_resolution)),
                         (int(715 * self.screen_resolution), int(200 * self.screen_resolution)), int(5 * self.screen_resolution))
        pygame.draw.line(self.screen, ('#FFFFFF'), (750 * self.screen_resolution, 200 * self.screen_resolution),
                         (int(780 * self.screen_resolution), int(200 * self.screen_resolution)), int(5 * self.screen_resolution))
        txt = q.render('Назад', True, (255, 255, 255))
        self.screen.blit(txt, (50 * self.screen_resolution, 545 * self.screen_resolution))
        txt = q.render('Разрешение', True, (255, 255, 255))
        self.screen.blit(txt, (20 * self.screen_resolution, 115 * self.screen_resolution))
        txt = q.render('Музыка', True, (255, 255, 255))
        self.screen.blit(txt, (440 * self.screen_resolution, 110 * self.screen_resolution))
        txt = q.render('Звуки', True, (255, 255, 255))
        self.screen.blit(txt, (445 * self.screen_resolution, 190 * self.screen_resolution))
        txt = q.render(f'{int(round(VOLUEME_M * 100,0))}%', True, (0, 0, 0))
        self.screen.blit(txt, (590 * self.screen_resolution, 110 * self.screen_resolution))
        txt = q.render(f'{int(round(VOLUEME_Z * 100, 0))}%', True, (0, 0, 0))
        self.screen.blit(txt, (590 * self.screen_resolution, 185 * self.screen_resolution))
        txt = q.render(f'{SCREEN_RESOLATION_LIST[SCREEN_RESOLATION_LIST[-1]]}', True, (0, 0, 0))
        self.screen.blit(txt, (225 * self.screen_resolution, 110 * self.screen_resolution))
        if (f):
            pygame.draw.rect(self.screen, ('#FFFFFF'), (185 * self.screen_resolution, 150 * self.screen_resolution,
                                                        150 * self.screen_resolution, 50 * self.screen_resolution))
            pygame.draw.rect(self.screen, ('#FFFFFF'), (185 * self.screen_resolution, 200 * self.screen_resolution,
                                                        150 * self.screen_resolution, 50 * self.screen_resolution))
            txt = q.render(f'{SCREEN_RESOLATION_LIST[0]}', True, (0, 0, 0))
            self.screen.blit(txt, (225 * self.screen_resolution, 160 * self.screen_resolution))
            txt = q.render(f'{SCREEN_RESOLATION_LIST[1]}', True, (0, 0, 0))
            self.screen.blit(txt, (225 * self.screen_resolution, 210 * self.screen_resolution))
        return list([[740 * self.screen_resolution, 100 * self.screen_resolution,
                      790 * self.screen_resolution, 150 * self.screen_resolution],
                     [675 * self.screen_resolution, 100 * self.screen_resolution,
                      735 * self.screen_resolution, 150 * self.screen_resolution],
                     [675 * self.screen_resolution, 175 * self.screen_resolution,
                      725 * self.screen_resolution, 225 * self.screen_resolution],
                     [740 * self.screen_resolution, 175 * self.screen_resolution,
                      790 * self.screen_resolution, 225 * self.screen_resolution],
                     [185 * self.screen_resolution, 100 * self.screen_resolution,
                      335 * self.screen_resolution, 150 * self.screen_resolution],
                     [185 * self.screen_resolution, 150 * self.screen_resolution,
                      335 * self.screen_resolution, 200 * self.screen_resolution],
                     [185 * self.screen_resolution, 200 * self.screen_resolution,
                      335 * self.screen_resolution, 250 * self.screen_resolution]])

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
        global SCREEN_RESOLATION_LIST
        if (q == 0):
            SCREEN_RESOLATION_LIST[-1] = 0
            return 1
        elif (q == 1):
            SCREEN_RESOLATION_LIST[-1] = 1
            return 1.2
