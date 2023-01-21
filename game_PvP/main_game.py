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


class TankGun(pygame.sprite.Sprite):
    def __init__(self, nm, team, body):
        super().__init__(all_sprites)
        if team == 'A':
            self.add(a_team)
        else:
            self.add(b_team)
        self.team = team
        self.name = 'gun'
        self.image = load_image(nm)
        self.image_orig = pygame.transform.scale(self.image, (54, 25))
        self.image = pygame.transform.scale(self.image, (54, 25))
        self.rect = self.image.get_rect()
        self.rect.move(body.rect.x, body.rect.y)
        self.ang = body.ang + 1
        self.body = body

    def update(self):
        self.image = pygame.transform.rotate(self.image_orig, -(self.ang / 0.017))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = self.body.rect.center


class BaseTank(pygame.sprite.Sprite):
    # image = load_image('tank_body.png')
    # image_orig = load_image('tank_body.png')
    # base scale 804x368

    def __init__(self, x, y, angle, nm, team):
        super().__init__(all_sprites)
        if team == 'A':
            self.add(a_team)
        else:
            self.add(b_team)
        self.team = team
        self.name = 'tonk'
        self.image = load_image(nm)
        self.image_orig = pygame.transform.scale(self.image, (67, 31))
        self.image = pygame.transform.scale(self.image, (67, 31))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.move(x, y)
        self.rect.x, self.rect.y = x, y
        self.ang = angle * 0.017
        self.crspeed = 0

    def update(self):
        self.rect = self.rect.move(self.crspeed * math.cos(self.ang),
                                           self.crspeed * math.sin(self.ang))
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.rotate(self.image_orig, -(self.ang / 0.017))
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.team == "A":
            for sprite in b_team:
                if pygame.sprite.spritecollideany(self, b_team) and \
                        pygame.sprite.spritecollideany(self, b_team).name == 'tonk' and \
                        pygame.sprite.collide_mask(self, sprite):
                    self.rect = self.rect.move(-self.crspeed * math.cos(self.ang), -self.crspeed * math.sin(self.ang))
                    self.crspeed = 0


class MainGame:
    def __init__(self, w, h, map=None):
        global width, height, all_sprites, player, barriers, a_team, b_team
        pygame.init()
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        a_team = pygame.sprite.Group()
        b_team = pygame.sprite.Group()
        barriers = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        clock = pygame.time.Clock()
        tank1 = BaseTank(100, 100, 0, 'tank_body.png', 'A')
        tank2 = BaseTank(300, 300, 0, 'tank_body.png', 'B')
        gun1 = TankGun('gun1.png', "A", tank1)
        gun2 = TankGun('gun1.png', "B", tank2)
        camera = Camera()
        running = True
        player = tank1
        m1 = False
        m2 = False
        maxspeed = 3
        k2 = 1
        k3 = 1
        while running:
            k = maxspeed / abs(player.crspeed if player.crspeed != 0 else 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        m1 = True
                        k2 = 1
                    if event.key == pygame.K_s:
                        m1 = True
                        k2 = -0.5
                    if event.key == pygame.K_a:
                        m2 = True
                        k3 = -1
                    if event.key == pygame.K_d:
                        m2 = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        m1 = False
                    if event.key == pygame.K_s:
                        m1 = False
                        k2 = 1
                    if event.key == pygame.K_a:
                        m2 = False
                        k3 = 1
                    if event.key == pygame.K_d:
                        m2 = False
            if m1 and abs(player.crspeed) < maxspeed:
                player.crspeed += 0.002 * k * k2
            else:
                if abs(player.crspeed) < 1:
                    player.crspeed = 0
                elif player.crspeed > 0:
                    player.crspeed -= 0.018
                elif player.crspeed < 0:
                    player.crspeed += 0.018
            if m2:
                player.ang += (0.6 * k3 * 0.017)
                player.ang = (player.ang / 0.017) % 360 * 0.017
            # print(player.crspeed, k, player.ang / 0.017)
            # debug out
            screen.fill((0, 0, 0))
            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            clock.tick(100)


if __name__ == '__main__':
    MainGame(800, 600)
