import pygame
from glavnoemenu import GlavnoeMenu
from newgame import Vibor
from  nastroiki import Nastroiki

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Главное меню')

    run = True
    q = GlavnoeMenu(screen)
    pos_knopok = []
    while run:
        pos_knopok = q.risovanie()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (q.type() == 'GlavnoeMenu'):
                    if (pos_knopok[0][0] <= event.pos[0] <= pos_knopok[0][2]
                            and pos_knopok[0][1] <= event.pos[1] <= pos_knopok[0][3]):
                        q = Vibor(screen)
                    elif (pos_knopok[1][0] <= event.pos[0] <= pos_knopok[1][2]
                            and pos_knopok[1][1] <= event.pos[1] <= pos_knopok[1][3]):
                        q = Nastroiki(screen)
                    elif (pos_knopok[2][0] <= event.pos[0] <= pos_knopok[2][2]
                            and pos_knopok[2][1] <= event.pos[1] <= pos_knopok[2][3]):
                        run = False
                        break
                elif (q.type() == 'Vibor'):
                    if (pos_knopok[0][0] <= event.pos[0] <= pos_knopok[0][2]
                            and pos_knopok[0][1] <= event.pos[1] <= pos_knopok[0][3]):
                        pass
                    elif (pos_knopok[1][0] <= event.pos[0] <= pos_knopok[1][2]
                            and pos_knopok[1][1] <= event.pos[1] <= pos_knopok[1][3]):
                        pass
                if (10 <= event.pos[0] <= 160 and 535 <= event.pos[1] <= 585
                and q.type() != 'GlavnoeMenu'):
                    q = GlavnoeMenu(screen)
        pygame.display.update()
    pygame.quit()