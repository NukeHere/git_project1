import pygame
import os
import sys
from glavnoemenu import GlavnoeMenu
from newgame import Vibor
from nastroiki import Nastroiki
from viborK import vibor_kart
from ypravlenie import Ypravlenie
from nastroiki import SCREEN_RESOLATION, VOLUEME_Z, VOLUEME_M, F


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Главное меню')

    run = True
    volueme_m = 1
    volueme_z = 1
    q = GlavnoeMenu(screen)
    pos_knopok = []
    pic = load_image("болото.png")
    cl = pygame.time.Clock()
    while run:
        pos_knopok = q.risovanie(pic)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (q.type() == 'GlavnoeMenu'):
                    if (pos_knopok[0][0] <= event.pos[0] <= pos_knopok[0][2]
                            and pos_knopok[0][1] <= event.pos[1] <= pos_knopok[0][3]):
                        q = Vibor(screen)
                        pic = load_image('голая земля.png')
                    elif (pos_knopok[1][0] <= event.pos[0] <= pos_knopok[1][2]
                          and pos_knopok[1][1] <= event.pos[1] <= pos_knopok[1][3]):
                        q = Nastroiki(screen)
                        pic = load_image('пустыня.png')
                    elif (pos_knopok[2][0] <= event.pos[0] <= pos_knopok[2][2]
                          and pos_knopok[2][1] <= event.pos[1] <= pos_knopok[2][3]):
                        q = Ypravlenie(screen)
                        pic = load_image('голая земля.png')
                    elif (pos_knopok[3][0] <= event.pos[0] <= pos_knopok[3][2]
                          and pos_knopok[3][1] <= event.pos[1] <= pos_knopok[3][3]):
                        run = False
                        break
                elif (q.type() == 'Vibor'):
                    if (pos_knopok[0][0] <= event.pos[0] <= pos_knopok[0][2]
                            and pos_knopok[0][1] <= event.pos[1] <= pos_knopok[0][3]):
                        q = vibor_kart(screen)
                    elif (pos_knopok[1][0] <= event.pos[0] <= pos_knopok[1][2]
                          and pos_knopok[1][1] <= event.pos[1] <= pos_knopok[1][3]):
                        q = vibor_kart(screen)
                elif (q.type() == 'Nastroiki'):
                    if (pos_knopok[0][0] <= event.pos[0] <= pos_knopok[0][2]
                            and pos_knopok[0][1] <= event.pos[1] <= pos_knopok[0][3]):
                        F = False
                        q.plusORminusZvuki(1, 0)
                    elif (pos_knopok[1][0] <= event.pos[0] <= pos_knopok[1][2]
                            and pos_knopok[1][1] <= event.pos[1] <= pos_knopok[1][3]):
                        F = False
                        q.plusORminusZvuki(0, 0)
                    elif (pos_knopok[2][0] <= event.pos[0] <= pos_knopok[2][2]
                            and pos_knopok[2][1] <= event.pos[1] <= pos_knopok[2][3]):
                        F = False
                        q.plusORminusZvuki(0, 1)
                    elif (pos_knopok[3][0] <= event.pos[0] <= pos_knopok[3][2]
                          and pos_knopok[3][1] <= event.pos[1] <= pos_knopok[3][3]):
                        F = False
                        q.plusORminusZvuki(1, 1)
                    elif (pos_knopok[4][0] <= event.pos[0] <= pos_knopok[4][2]
                          and pos_knopok[4][1] <= event.pos[1] <= pos_knopok[4][3]):
                        F = True
                        q.risovanie2()
                if (10 <= event.pos[0] <= 160 and 535 <= event.pos[1] <= 585
                        and q.type() != 'GlavnoeMenu'):
                    F = False
                    q = GlavnoeMenu(screen)
                    pic = load_image("болото.png")
        pygame.display.update()
    pygame.quit()
