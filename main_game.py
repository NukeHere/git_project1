import pygame
import os
import sys
import math


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 100
        self.dy = 100

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)

class BaseTank(pygame.sprite.Sprite):
    #image = load_image('tank_body.png')

    # base scale 804x368

    def __init__(self, x, y, angle, nm):
        super().__init__(all_sprites)
        BaseTank.image = load_image(nm)
        BaseTank.image = pygame.transform.scale(BaseTank.image, (201, 92))
        self.image = BaseTank.image
        self.rect = self.image.get_rect()
        self.rect.move(x, y)
        self.rect.x, self.rect.y = x, y
        self.ang = angle * 0.017
        self.mxspeed = 2

    def update(self):
        if moving and self == player:
            player.rect = player.rect.move(-player.mxspeed * math.cos(player.ang),
                                           player.mxspeed * math.sin(player.ang))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    tank1 = BaseTank(100, 100, 90, 'tank_body.png')
    tank2 = BaseTank(500, 500, 0, 'nlo.jpg')
    camera = Camera()
    running = True
    player = tank1
    moving = False
    while running:
        print(tank2.rect.x, tank2.rect.y, camera.dx, camera.dy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    moving = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    moving = False
        screen.fill((0, 0, 0))
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(100)
