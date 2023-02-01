import pygame
import os
import sys
import math
from collections import deque


# from main import VOLUEME_M, VOLUEME_Z


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class AI:
    def __init__(self, map1, aimb, aimg, body):
        self.mp = map1
        self.mp1 = self.mp[:]
        self.aim1 = aimb
        self.aim2 = aimg
        self.bd = body
        self.tm = 0
        self.path = []
        self.i = 0
        self.aim2.ai = self

    def update(self):
        def bfs():
            plcoords = (player.rect.x + 1) // 50 + (player.rect.y + 1) // 50 * 40
            #print(plcoords)
            d = deque()
            cur2 = (self.bd.rect.x + 1) // 50 + (self.bd.rect.y + 1) // 50 * 40
            cur = cur2 + 1 - 1
            #print(cur)
            self.mp1 = self.mp[:]
            self.mp1[cur][0] = 1
            while cur != plcoords:
                if cur not in [i for i in range(40)] + [i for i in range(1559, 1600)] + [i * 40 for i in range(40)] + [i * 40 - 1 for i in range(1, 41)]:
                    if 2000 > self.mp1[cur - 1][0] > self.mp1[cur][0] + 1 or self.mp1[cur - 1][0] == 0:
                        d.append(cur - 1)
                        self.mp1[cur - 1] = [self.mp1[cur][0] + 1, cur]
                    if 2000 > self.mp1[cur + 1][0] > self.mp1[cur][0] + 1 or self.mp1[cur + 1][0] == 0:
                        d.append(cur + 1)
                        self.mp1[cur + 1] = [self.mp1[cur][0] + 1, cur]
                    if 2000 > self.mp1[cur - 40][0] > self.mp1[cur][0] + 1 or self.mp1[cur - 40][0] == 0:
                        d.append(cur - 40)
                        self.mp1[cur - 40] = [self.mp1[cur][0] + 1, cur]
                    if 2000 > self.mp1[cur + 40][0] > self.mp1[cur][0] + 1 or self.mp1[cur + 40][0] == 0:
                        d.append(cur + 40)
                        self.mp1[cur + 40] = [self.mp1[cur][0] + 1, cur]
                    #if cur == 409:
                        #print(self.mp1[cur + 1], self.mp1[cur - 1], self.mp1[cur])
                if len(d) == 0:
                    cur2 = plcoords
                    break
                cur = d.popleft()
            l = [plcoords]
            cur = plcoords
            while cur != cur2:
                #print(cur)
                cur = self.mp1[cur][1]
                l.append(cur)
            return l

        if timer >= self.tm:
            self.tm = timer + 5
            self.path = bfs()
        if len(self.path) != 0 and (self.bd.rect.x + 1) // 50 + (self.bd.rect.y + 1) // 50 * 40 == self.path[self.i]:
            if self.i + 1 == len(self.path):
                self.tm = 0
            else:
                self.i += 1


class GameObj(pygame.sprite.Sprite):
    def __init__(self, nm, x, y, w, h, col=False, col_map=None):
        super().__init__(all_sprites)
        self.name = 'obj'
        self.image = load_image(nm)
        self.image_orig = pygame.transform.scale(self.image, (w, h))
        self.image = pygame.transform.scale(self.image, (w, h))
        if col:
            self.rect = self.image.get_rect()
            self.colmp = col_map
        else:
            self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.x, self.rect.y = x, y


class Textrender:
    def __init__(self, screen, screen_resolution):
        self.screen = screen
        self.screen_resolution = screen_resolution

    def risovanie(self):
        pygame.font.init()
        pygame.draw.rect(self.screen, ('#808080'), (10 * self.screen_resolution,
                                                    560 * self.screen_resolution, 135 * self.screen_resolution,
                                                    40 * self.screen_resolution))
        pygame.draw.rect(self.screen, ('#808080'), (645 * self.screen_resolution,
                                                    560 * self.screen_resolution, 145 * self.screen_resolution,
                                                    40 * self.screen_resolution))
        q = pygame.font.SysFont('arial', int(25 * self.screen_resolution))
        txt = q.render('Твои XP: ' + str(100), True, (255, 255, 255))
        self.screen.blit(txt, (15 * self.screen_resolution,
                               565 * self.screen_resolution))
        txt = q.render('XP врага: ' + str(100), True, (255, 255, 255))
        self.screen.blit(txt, (650 * self.screen_resolution,
                               565 * self.screen_resolution))


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


class Track(pygame.sprite.Sprite):
    def __init__(self, nm, nm2, team, body, armour, start_ang):
        super().__init__(all_sprites)
        if team == 'A':
            self.add(a_team)
        else:
            self.add(b_team)
        self.team = team
        self.name = 'track'
        self.image = load_image(nm)
        self.image_orig = pygame.transform.scale(self.image, (67, 65))
        self.image = pygame.transform.scale(self.image, (67, 65))
        self.image2 = pygame.transform.scale(load_image(nm2), (67, 65))
        self.rect = self.image.get_rect()
        self.rect.move(body.rect.x, body.rect.y)
        self.ang = body.ang + 1
        self.body = body
        self.stang = start_ang * 0.017
        self.armour = armour
        self.repd = True
        self.tm = 0

    def update(self):
        self.ang = self.body.ang + self.stang
        if self.repd:
            self.image = pygame.transform.rotate(self.image_orig, -(self.ang / 0.017))
        else:
            self.image = pygame.transform.rotate(self.image2, -(self.ang / 0.017))
            if timer >= self.tm:
                self.tm = 0
                self.repd = True
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = self.body.rect.center
        self.mask = pygame.mask.from_surface(self.image)

    def xpd(self, dmg):
        if self.repd:
            self.repd = False
            self.body.xp -= dmg
        self.tm = timer + 5


class Ammo(pygame.sprite.Sprite):
    # image = load_image('tank_body.png')
    # image_orig = load_image('tank_body.png')
    # base scale 804x368

    def __init__(self, nm, team, ang, pos, bs_dmg=20, sp=20):
        super().__init__(all_sprites)
        if team == 'A':
            self.add(a_team)
        else:
            self.add(b_team)
        self.team = team
        self.name = 'bul'
        self.image = load_image(nm)
        self.image_orig = pygame.transform.scale(self.image, (13, 7))
        self.image = pygame.transform.scale(self.image, (13, 7))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.ang = ang
        self.crspeed = sp
        self.bs_dmg = bs_dmg
        self.rect.x, self.rect.y = pos

    def update(self):
        self.rect = self.rect.move(self.crspeed * math.cos(self.ang),
                                   self.crspeed * math.sin(self.ang))
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.rotate(self.image_orig, -(self.ang / 0.017))
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.team == "A":
            for sprite in b_team:
                if pygame.sprite.spritecollideany(self, b_team) and pygame.sprite.collide_mask(self, sprite):
                    if sprite.name not in ['bul', 'Aim', 'tonk']:
                        sprite.xpd(max(self.bs_dmg // 2 - sprite.armour, 0))
                    if sprite.name == 'tonk':
                        sprite.xpd(max(self.bs_dmg - sprite.armour, 0))
                        self.image = load_image('null.png')
                        self.crspeed = 0
                        self.remove(a_team)
                        self.remove(all_sprites)
        if self.team == "B":
            for sprite in a_team:
                if pygame.sprite.spritecollideany(self, a_team) and pygame.sprite.collide_mask(self, sprite):
                    if sprite.name not in ['bul', 'Aim']:
                        sprite.xp -= max(self.bs_dmg // 2 - sprite.armour, 0)
                    if sprite.name == 'tonk':
                        sprite.xp -= max(self.bs_dmg - sprite.armour, 0)
                        self.image = load_image('null.png')
                        self.crspeed = 0
                        self.remove(b_team)
                        self.remove(all_sprites)


class Aim(pygame.sprite.Sprite):

    def __init__(self, team, is_ai=False, aim=False, ai=None):
        super().__init__(all_sprites)
        if team == 'A':
            self.add(a_team)
        else:
            self.add(b_team)
        self.add(aims)
        self.team = team
        self.name = 'Aim'
        self.rect = pygame.Rect(1, 1, 1, 1)
        self.aimode = is_ai
        self.aim = aim
        self.image = load_image('null.png')
        self.ai = ai

    def update(self):
        if self.aimode and self.aim:
            self.rect.x, self.rect.y = player.rect.center
        elif self.aimode and not self.aim and self.ai:
            if len(self.ai.path) != 0:
                self.rect.x, self.rect.y = 50 * self.ai.path[self.ai.i] % 40, 50 * self.ai.path[self.ai.i] // 40
            else:
                self.rect.x, self.rect.y = 500, 500

    def mousemoved(self, pos):
        if not self.aimode:
            self.rect.x, self.rect.y = pos


class TankGun(pygame.sprite.Sprite):
    def __init__(self, nm, team, body, aim, armour):
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
        self.aim = aim
        self.armour = armour

    def update(self):
        self.image = pygame.transform.rotate(self.image_orig, -(self.ang / 0.017))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.center = self.body.rect.center
        self.mask = pygame.mask.from_surface(self.image)
        kk = math.atan(
            (self.aim.rect.x - self.rect.center[0] + 0.0001) / (self.aim.rect.y - self.rect.center[1] + 0.0001))
        if self.aim.rect.y < self.rect.center[1]:
            if self.aim.rect.x > self.rect.center[0]:
                kk = -(90 * 0.017 + kk)
            else:
                kk = -90 * 0.017 - kk
        else:
            kk = 90 * 0.017 - kk
        if self.ang > 180 * 0.017:
            self.ang = -180 * 0.017
        elif self.ang < -180 * 0.017:
            self.ang = 180 * 0.017
        if self.ang != kk:
            e1 = 0
            e2 = 0
            if self.ang > 0:
                if kk > 0:
                    e1 = -self.ang + kk if kk > self.ang else 3.06 - self.ang + kk + 3.06
                    e2 = self.ang - kk if self.ang > kk else 3.06 - self.ang + kk + 3.06
                else:
                    e1 = 3.06 - self.ang - kk
                    e2 = self.ang - kk
            else:
                if kk > 0:
                    e1 += -self.ang + kk
                    e2 += 3.06 + self.ang + 3.06 - self.ang
                else:
                    e1 += -self.ang + kk if self.ang < kk else self.ang + 3.06 + 3.06 - kk
                    e2 += self.ang - kk if self.ang > kk else 3.06 + 3.06 - self.ang + kk
            if abs(self.ang - kk) <= 0.017:
                self.ang = kk
            elif e1 <= e2:
                # self.ang < kk or
                self.ang += 0.017 * 1
            else:
                self.ang -= 0.017 * 1
            # print(self.ang / 0.017, kk / 0.017, e1, e2) debug out

    def fire(self):
        Ammo('bul.png', self.team, self.ang, self.rect.center, sp=10)

    def xpd(self, dmg):
        self.body.xp -= dmg


class BaseTank(pygame.sprite.Sprite):
    # image = load_image('tank_body.png')
    # image_orig = load_image('tank_body.png')
    # base scale 804x368

    def __init__(self, x, y, angle, nm, team, armour, xp, aim=None):
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
        self.armour = armour
        self.xp = xp
        self.aim = aim

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
        if self.team == "B":
            for sprite in a_team:
                if pygame.sprite.spritecollideany(self, a_team) and \
                        pygame.sprite.spritecollideany(self, a_team).name == 'tonk' and \
                        pygame.sprite.collide_mask(self, sprite):
                    self.rect = self.rect.move(-self.crspeed * math.cos(self.ang), -self.crspeed * math.sin(self.ang))
                    self.crspeed = 0
        if self.aim:
            self.rect.x, self.rect.y = self.aim.rect.center

    def xpd(self, dmg):
        self.xp -= dmg


class MainGame:
    def __init__(self, w, h, maap=None):
        global width, height, all_sprites, player, barriers, a_team, b_team, aims, timer
        VOLUEME_M, VOLUEME_Z = 1, 1
        timer = 0
        pygame.init()
        size = width, height = w, h
        sound_battle = pygame.mixer.Sound(os.path.join('data',
                                                       'Andrey Kulik feat. Andrius Klimka and Vyacheslav Skadorva - Mountain Pass (Battle).mp3'))
        sound_fire = pygame.mixer.Sound(os.path.join('data', 'выстрел.mp3'))
        sound_fire.set_volume(VOLUEME_Z)
        sound_battle.set_volume(VOLUEME_M)
        screen = pygame.display.set_mode(size)
        aims = pygame.sprite.Group()
        a_team = pygame.sprite.Group()
        b_team = pygame.sprite.Group()
        barriers = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        clock = pygame.time.Clock()
        if maap == None:
            maap = [GameObj('болото.png', 0, 0, 500, 500), GameObj('болото.png', 0, 500, 500, 500),
                    GameObj('болото.png', 500, 0, 500, 500), GameObj('болото.png', 500, 500, 500, 500)]
        tank1 = BaseTank(300, 300, 0, 'tank_body.png', 'A', 16, 100)
        tank2 = BaseTank(500, 500, 0, 'tank_body.png', 'B', 16, 100)
        track11 = Track('track1.png', 'track2.png', "A", tank1, 8, 0)
        track12 = Track('track1.png', 'track2.png', "A", tank1, 8, 180)
        track21 = Track('track1.png', 'track2.png', "B", tank2, 8, 0)
        track22 = Track('track1.png', 'track2.png', "B", tank2, 8, 180)
        ai1 = Aim("A")
        ai2 = Aim("B", is_ai=True, aim=True)
        ai3 = Aim('b', is_ai=True, aim=False)
        tank2.aim = ai3
        gun1 = TankGun('gun1.png', "A", tank1, ai1, 8)
        gun2 = TankGun('gun1.png', "B", tank2, ai2, 8)
        camera = Camera()
        ai11 = AI([[i, 0] for i in range(1600)], ai3, ai2, tank2)
        running = True
        player = tank1
        m1 = False
        m2 = False
        maxspeed = 3
        k2 = 1
        k3 = 1
        mousepos = (0, 0)
        sound_battle.play(-1)
        t = Textrender(screen, screen_resolution=w / 800)
        while running:
            print(tank2.rect.x, tank2.rect.y, tank1.rect.x, tank1.rect.y)
            ai11.update()
            timer += 0.01
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
                if event.type == pygame.MOUSEMOTION:
                    mousepos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gun1.fire()
                    sound_fire.play(0)
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
            screen.fill((0, 0, 0))
            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)
            for spr in aims:
                spr.mousemoved(mousepos)
            all_sprites.update()
            all_sprites.draw(screen)
            t.risovanie()
            pygame.display.flip()
            clock.tick(100)


if __name__ == '__main__':
    MainGame(800, 600)
