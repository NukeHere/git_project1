import pygame
import os
import sys
from glavnoemenu import GlavnoeMenu
from newgame import Vibor
from nastroiki import Nastroiki
from viborK import vibor_kart
from ypravlenie import Ypravlenie
from nastroiki import VOLUEME_Z, VOLUEME_M


SCREEN_RESOLATION = 1


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800 * SCREEN_RESOLATION, 600 * SCREEN_RESOLATION
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Главное меню')

    run = True
    volueme_m = 1
    volueme_z = 1
    q = GlavnoeMenu(screen, SCREEN_RESOLATION)
    pos_knopok = []
    pic = load_image("болото.png")
    f = True
    while run:
        if(f):
            pos_knopok = q.risovanie(pic)
        else:
            pos_knopok = q.risovanie(pic, True)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (q.type() == 'GlavnoeMenu'):
                    if (pos_knopok[0][0] <= event.pos[0] <= pos_knopok[0][2]
                            and pos_knopok[0][1] <= event.pos[1] <= pos_knopok[0][3]):
                        q = Vibor(screen, SCREEN_RESOLATION)
                        pic = load_image('голая земля.png')
                    elif (pos_knopok[1][0] <= event.pos[0] <= pos_knopok[1][2]
                          and pos_knopok[1][1] <= event.pos[1] <= pos_knopok[1][3]):
                        q = Nastroiki(screen, SCREEN_RESOLATION)
                        pic = load_image('пустыня.png')
                    elif (pos_knopok[2][0] <= event.pos[0] <= pos_knopok[2][2]
                          and pos_knopok[2][1] <= event.pos[1] <= pos_knopok[2][3]):
                        q = Ypravlenie(screen, SCREEN_RESOLATION)
                        pic = load_image('голая земля.png')
                    elif (pos_knopok[3][0] <= event.pos[0] <= pos_knopok[3][2]
                          and pos_knopok[3][1] <= event.pos[1] <= pos_knopok[3][3]):
                        run = False
                        break
                elif (q.type() == 'Vibor'):
                    if (pos_knopok[0][0] <= event.pos[0] <= pos_knopok[0][2]
                            and pos_knopok[0][1] <= event.pos[1] <= pos_knopok[0][3]):
                        q = vibor_kart(screen, SCREEN_RESOLATION)
                    elif (pos_knopok[1][0] <= event.pos[0] <= pos_knopok[1][2]
                          and pos_knopok[1][1] <= event.pos[1] <= pos_knopok[1][3]):
                        q = vibor_kart(screen, SCREEN_RESOLATION)
                elif (q.type() == 'Nastroiki'):
                    if (not f):
                        if (pos_knopok[5][0] <= event.pos[0] <= pos_knopok[5][2]
                            and pos_knopok[5][1] <= event.pos[1] <= pos_knopok[5][3]):
                            SCREEN_RESOLATION = q.new_resolution(0)
                            size = width, height = 800 * SCREEN_RESOLATION, 600 * SCREEN_RESOLATION
                            screen = pygame.display.set_mode(size)
                            pos_knopok = q.risovanie(pic)
                            pygame.display.update()
                        elif (pos_knopok[6][0] <= event.pos[0] <= pos_knopok[6][2]
                            and pos_knopok[6][1] <= event.pos[1] <= pos_knopok[6][3]):
                            SCREEN_RESOLATION = q.new_resolution(1)
                            print(SCREEN_RESOLATION)
                            size = width, height = 800 * SCREEN_RESOLATION, 600 * SCREEN_RESOLATION
                            screen = pygame.display.set_mode(size)
                            pos_knopok = q.risovanie(pic)
                            pygame.display.update()
                    if (pos_knopok[0][0] <= event.pos[0] <= pos_knopok[0][2]
                            and pos_knopok[0][1] <= event.pos[1] <= pos_knopok[0][3]):
                        q.plusORminusZvuki(1, 0)
                        f = True
                    elif (pos_knopok[1][0] <= event.pos[0] <= pos_knopok[1][2]
                            and pos_knopok[1][1] <= event.pos[1] <= pos_knopok[1][3]):
                        q.plusORminusZvuki(0, 0)
                        f = True
                    elif (pos_knopok[2][0] <= event.pos[0] <= pos_knopok[2][2]
                            and pos_knopok[2][1] <= event.pos[1] <= pos_knopok[2][3]):
                        q.plusORminusZvuki(0, 1)
                        f = True
                    elif (pos_knopok[3][0] <= event.pos[0] <= pos_knopok[3][2]
                          and pos_knopok[3][1] <= event.pos[1] <= pos_knopok[3][3]):
                        q.plusORminusZvuki(1, 1)
                        f = True
                    elif (pos_knopok[4][0] <= event.pos[0] <= pos_knopok[4][2]
                          and pos_knopok[4][1] <= event.pos[1] <= pos_knopok[4][3]):
                        f = False
                    else:
                        f = True
                if (10 * SCREEN_RESOLATION <= event.pos[0] <= 160 * SCREEN_RESOLATION
                        and 535 * SCREEN_RESOLATION <= event.pos[1] <= 585 * SCREEN_RESOLATION
                        and q.type() != 'GlavnoeMenu'):
                    F = False
                    q = GlavnoeMenu(screen, SCREEN_RESOLATION)
                    pic = load_image("болото.png")
        pygame.display.update()
    pygame.quit()
