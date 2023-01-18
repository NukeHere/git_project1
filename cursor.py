import pygame
import os
import sys


pygame.init()
width = 500
height = 500
size = 500, 500
screen = pygame.display.set_mode(size)
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    pos = pygame.mouse.get_pos()
    image = load_image('arrow.png')
    pygame.mouse.set_visible(False)
    cursor_img_rect = image.get_rect()
    if pygame.mouse.get_focused():
        screen.blit(image, pos)
    pygame.display.flip()
pygame.quit()
