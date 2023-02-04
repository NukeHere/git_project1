import pygame
import os
import sys
import math
import random
from collections import deque


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class AI:
    def __init__(self, map1, aimb, gun, body):
        self.mp = map1
        self.mp1 = self.mp[:]
        self.aim1 = aimb
        self.gun = gun
        self.bd = body
        self.tm = 0
        self.path = []
        self.i = 0
        self.tm2 = 10

    def update(self):
        def bfs():
            plcoords = (player.rect.x - delta.rect.x) // 50 + (player.rect.y - delta.rect.y) // 50 * 40
            d = deque()
            cur2 = (self.bd.rect.x - delta.rect.x) // 50 + (self.bd.rect.y - delta.rect.y) // 50 * 40
            if cur2 < 0:
                return [plcoords]
            cur = cur2 + 1 - 1
            self.mp1 = self.mp[:]
            self.mp1[cur][0] = 1
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
            while len(d) > 0:
                if cur % 40 != 0 and (2000 > self.mp1[cur - 1][0] > self.mp1[cur][0] + 1 or self.mp1[cur - 1][0] == 0):
                    d.append(cur - 1)
                    self.mp1[cur - 1] = [self.mp1[cur][0] + 1, cur]
                if cur % 40 != 39 and (2000 > self.mp1[cur + 1][0] > self.mp1[cur][0] + 1 or self.mp1[cur + 1][0] == 0):
                    d.append(cur + 1)
                    self.mp1[cur + 1] = [self.mp1[cur][0] + 1, cur]
                if cur > 39 and (2000 > self.mp1[cur - 40][0] > self.mp1[cur][0] + 1 or self.mp1[cur - 40][0] == 0):
                    d.append(cur - 40)
                    self.mp1[cur - 40] = [self.mp1[cur][0] + 1, cur]
                if cur < 1560 and (2000 > self.mp1[cur + 40][0] > self.mp1[cur][0] + 1 or self.mp1[cur + 40][0] == 0):
                    d.append(cur + 40)
                    self.mp1[cur + 40] = [self.mp1[cur][0] + 1, cur]
                cur = d.popleft()
            l = []
            if plcoords not in [i for i in range(80)] + [i for i in range(1559, 1600)] + [i for i in
                                                                                          range(0, 1600, 40)] + \
                    [i + 40 for i in range(0, 1600, 40)]:
                l = [plcoords]
            cur = plcoords
            i = 0
            while cur != cur2 and i < 2000:
                cur = self.mp1[cur][1]
                if cur not in [i for i in range(40)] + [i for i in range(1559, 1600)] + [i for i in
                                                                                         range(0, 1600, 40)] + \
                        [i + 39 for i in range(0, 1600, 40)]:
                    l.append(cur)
                i += 1
            return l[::-1]

        if timer >= self.tm or self.i == len(self.path) - 1 and self.bd.xp > 0:
            self.path = bfs()
            self.tm = timer + min(3, len(self.path) // 4)
            self.i = 0

        if timer >= self.tm2 and self.bd.xp > 0:
            self.gun.fire()
            self.tm2 = timer + max(5, (((player.rect.x - self.bd.rect.x) ** 2 +
                                        (player.rect.y - self.bd.rect.y) ** 2) ** 0.5) / 600 * 5)


class GameObj(pygame.sprite.Sprite):
    def __init__(self, nm, x, y, w, h, col=False, col_map=None):
        super().__init__(all_sprites)
        self.name = 'obj'
        self.image = load_image(nm)
        self.image_orig = pygame.transform.scale(self.image, (w, h))
        self.image = pygame.transform.scale(self.image, (w, h))
        if col:
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.colmp = col_map
            self.add(statick)
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
        txt = q.render('Твои XP: ' + str(player.xp), True, (255, 255, 255))
        self.screen.blit(txt, (15 * self.screen_resolution,
                               565 * self.screen_resolution))
        txt = q.render('XP врага: ' + str(cur_fps), True, (255, 255, 255))
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
            self.body.repd = False
            if timer >= self.tm:
                self.tm = 0
                self.repd = True
                self.body.repd = True
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
                        if sprite.xp > 0:
                            random.choice((sound_probitie, sound_probitie2)).play(0)
                        self.image = load_image('null.png')
                        self.crspeed = 0
                        self.remove(a_team)
                        self.remove(all_sprites)
        if self.team == "B":
            for sprite in a_team:
                if pygame.sprite.spritecollideany(self, a_team) and pygame.sprite.collide_mask(self, sprite):
                    if sprite.name not in ['bul', 'Aim']:
                        sprite.xpd(max(self.bs_dmg // 2 - sprite.armour, 0))
                    if sprite.name == 'tonk':
                        sprite.xpd(max(self.bs_dmg - sprite.armour, 0))
                        if sprite.xp > 0:
                            random.choice((sound_pr1, sound_pr2, sound_pr3)).play(0)
                        self.image = load_image('null.png')
                        self.crspeed = 0
                        self.remove(b_team)
                        self.remove(all_sprites)
        for sprite in statick:
            if pygame.sprite.collide_mask(self, sprite):
                sound_fire_exp.play(0)
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
        self.tm = 0

    def update(self):
        if self.aimode and self.aim:
            self.rect.x, self.rect.y = player.rect.center
        if self.aimode and not self.aim and self.ai:
            if len(self.ai.path) != 0:
                self.rect.x, self.rect.y = 50 * (self.ai.path[self.ai.i] % 40) + delta.rect.x + 25, \
                                           50 * (self.ai.path[self.ai.i] // 40) + delta.rect.y + 25

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
        if self.body.xp > 0:
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
                    self.ang += 0.017 * 1 * (100 / max(1, int(cur_fps)))
                else:
                    self.ang -= 0.017 * 1 * (100 / max(1, int(cur_fps)))
                # print(self.ang / 0.017, kk / 0.017, e1, e2) debug out

    def fire(self):
        sound_fire.play(0)
        Ammo('bul.png', self.team, self.ang, self.rect.center, sp=10, bs_dmg=30)

    def xpd(self, dmg):
        self.body.xp -= dmg


class BaseTank(pygame.sprite.Sprite):
    # image = load_image('tank_body.png')
    # image_orig = load_image('tank_body.png')
    # base scale 804x368

    def __init__(self, x, y, angle, nm, team, armour, xp, maxspeed, aim=None):
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
        self.repd = True
        self.m1 = 0
        self.m2 = 0
        self.k = 0
        self.k2 = 0
        self.k3 = 0
        self.maxspeed = maxspeed

    def update(self):
        k = 1
        if self.xp > 0:
            if self.repd:
                self.rect = self.rect.move(self.crspeed * math.cos(self.ang),
                                           self.crspeed * math.sin(self.ang))
            else:
                self.crspeed = 0
                k = 0.4
            self.mask = pygame.mask.from_surface(self.image)
            self.image = pygame.transform.rotate(self.image_orig, -(self.ang / 0.017))
            self.rect = self.image.get_rect(center=self.rect.center)
            if self.team == "A":
                for sprite in b_team:
                    if pygame.sprite.spritecollideany(self, b_team) and \
                            pygame.sprite.spritecollideany(self, b_team).name == 'tonk' and \
                            pygame.sprite.collide_mask(self, sprite):
                        self.rect = self.rect.move(-self.crspeed * math.cos(self.ang),
                                                   -self.crspeed * math.sin(self.ang))
                        self.crspeed = 0
            if self.team == "B":
                for sprite in a_team:
                    if pygame.sprite.spritecollideany(self, a_team) and \
                            pygame.sprite.spritecollideany(self, a_team).name == 'tonk' and \
                            pygame.sprite.collide_mask(self, sprite):
                        self.rect = self.rect.move(-self.crspeed * math.cos(self.ang),
                                                   -self.crspeed * math.sin(self.ang))
                        self.crspeed = 0
            for sprite in statick:
                if pygame.sprite.collide_mask(self, sprite):
                    self.rect = self.rect.move(-self.crspeed * math.cos(self.ang), -self.crspeed * math.sin(self.ang))
                    self.crspeed = 0
                    if self != player:
                        self.rect = self.rect.move(-self.maxspeed * math.cos(self.ang),
                                                   -self.maxspeed * math.sin(self.ang))
                        if pygame.sprite.collide_mask(self, sprite):
                            self.rect = self.rect.move(self.maxspeed * math.cos(self.ang),
                                                       self.maxspeed * math.sin(self.ang))
                            self.rect = self.rect.move(self.maxspeed * math.cos(self.ang),
                                                       self.maxspeed * math.sin(self.ang))
                            if pygame.sprite.collide_mask(self, sprite):
                                self.rect = self.rect.move(-self.maxspeed * math.cos(self.ang),
                                                           -self.maxspeed * math.sin(self.ang))

            if self.aim:
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
                        self.ang += 0.017 * k * (100 / max(1, int(cur_fps)))
                    else:
                        self.ang -= 0.017 * k * (100 / max(1, int(cur_fps)))
                if (self.rect.center[0] - delta.rect.x + 1) // 50 + (
                        self.rect.center[1] - delta.rect.y + 1) // 50 * 40 != \
                        (self.aim.rect.x - delta.rect.x + 1) // 50 + (self.aim.rect.y - delta.rect.y + 1) // 50 * 40:
                    if abs(self.ang - kk) <= 0.017 * k and self.crspeed < self.maxspeed:
                        if self.crspeed < 1:
                            self.crspeed = 1
                        self.crspeed += 0.012 * (100 / max(1, int(cur_fps)))
                    elif self.crspeed > 0.006:
                        self.crspeed -= 0.006 / k * (100 / max(1, int(cur_fps)))
                else:
                    if self.crspeed > 0.02:
                        self.crspeed -= 0.012 / k * (100 / max(1, int(cur_fps)))
                    else:
                        self.crspeed = 0
                    if self.aim.ai.i < len(self.aim.ai.path) - 1:
                        self.aim.ai.i += 1
            else:
                self.maxspeed = 3
                if self.m1 and abs(self.crspeed) < self.maxspeed:
                    self.crspeed += 0.003 * self.k * self.k2 * (100 / max(1, int(cur_fps)))
                else:
                    if abs(self.crspeed) < 1:
                        self.crspeed = 0
                    elif self.crspeed > 0:
                        self.crspeed -= 0.018 * (100 / max(1, int(cur_fps)))
                    elif self.crspeed < 0:
                        self.crspeed += 0.018 * (100 / max(1, int(cur_fps)))
                if self.m2:
                    self.ang += (0.6 * self.k3 * 0.017) * (100 / max(1, int(cur_fps))) * k
                    self.ang = (self.ang / 0.017) % 360 * 0.017
        elif self.xp < 0:
            self.xp = 0

    def xpd(self, dmg):
        if self.xp > 0:
            self.xp -= dmg
            if self.xp <= 0:
                if self.team == "A":
                    self.remove(a_team)
                    sound_1 = pygame.mixer.Sound(os.path.join('data', 'tank-destr.mp3'))
                    sound_1.play(0)
                else:
                    self.remove(b_team)
                    sound_1 = pygame.mixer.Sound(os.path.join('data', 'wot_bigboom_far.mp3'))
                    sound_1.play(0)
                self.add(statick)
                self.image = load_image('tank_body2.png')
                self.image = pygame.transform.scale(self.image, (67, 31))
                self.image = pygame.transform.rotate(self.image, -(self.ang / 0.017))

    def givekf(self, m1, m2, k, k2, k3):
        self.m1 = m1
        self.m2 = m2
        self.k = k
        self.k2 = k2
        self.k3 = k3


class MainGame:
    def __init__(self, w, h, maap, spr, so):
        global width, height, all_sprites, player, barriers, a_team, b_team, aims, timer, cur_fps, delta, statick, \
            sound_fire, sound_fire_exp, sound_probitie, sound_pr1, sound_pr2, sound_pr3, sound_probitie2
        timer = 0
        pygame.init()
        size = width, height = w, h
        VOLUEME_M, VOLUEME_Z = so
        sound_battle = pygame.mixer.Sound(os.path.join('data',
                                                       'Andrey Kulik feat. Andrius Klimka and Vyacheslav Skadorva - Mountain Pass (Battle).mp3'))
        sound_fire = pygame.mixer.Sound(os.path.join('data', 'выстрел.mp3'))
        sound_pr1 = pygame.mixer.Sound(os.path.join('data', '1.mp3'))
        sound_pr2 = pygame.mixer.Sound(os.path.join('data', '2.mp3'))
        sound_pr3 = pygame.mixer.Sound(os.path.join('data', '4.mp3'))
        sound_probitie = pygame.mixer.Sound(os.path.join('data', 'probitie1.mp3'))
        sound_probitie2 = pygame.mixer.Sound(os.path.join('data', 'probitie-2.mp3'))
        sound_fire_exp = pygame.mixer.Sound(os.path.join('data', 'взрыв.mp3'))
        sound_probitie.set_volume(VOLUEME_Z)
        sound_fire.set_volume(VOLUEME_Z)
        sound_fire_exp.set_volume(VOLUEME_Z)
        sound_battle.set_volume(VOLUEME_M)
        screen = pygame.display.set_mode(size)
        aims = pygame.sprite.Group()
        a_team = pygame.sprite.Group()
        b_team = pygame.sprite.Group()
        barriers = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        statick = pygame.sprite.Group()
        clock = pygame.time.Clock()
        maap2 = []
        maap = list(maap)[1:]
        print(maap)
        maapai = [[i, 0] for i in range(1600)]
        for i in maap:
            ls = i[0].split(':')
            if ls[0] == 'random':
                ls = random.choice(ls[1:])
            maap2.append(GameObj(ls, int(i[1]), int(i[2]),
                                 int(i[3].split('x')[0]) * 50, int(i[3].split('x')[1]) * 50,
                                 col=True, col_map=[i[3].split('x')[0], i[3].split('x')[1]]))
            coords = int(i[1]) // 50 + int(i[2]) // 50 * 40
            for y in range(int(i[3].split('x')[1])):
                for x in range(int(i[3].split('x')[0])):
                    maapai[coords + y * 40 + x] = [2500, 0]
        maap = maap2
        """[GameObj('болото.png', 0, 0, 500, 500), GameObj('болото.png', 0, 500, 500, 500),
                GameObj('болото.png', 500, 0, 500, 500), GameObj('болото.png', 500, 500, 500, 500),
                GameObj('болото.png', 1000, 0, 500, 500), GameObj('болото.png', 1000, 500, 500, 500),
                GameObj('болото.png', 1500, 0, 500, 500), GameObj('болото.png', 1500, 500, 500, 500),
                GameObj('болото.png', 0, 2000, 500, 500), GameObj('болото.png', 0, 2500, 500, 500),
                GameObj('болото.png', 500, 2000, 500, 500), GameObj('болото.png', 500, 2500, 500, 500),
                GameObj('болото.png', 1000, 2000, 500, 500), GameObj('болото.png', 1000, 2500, 500, 500),
                GameObj('болото.png', 1500, 2000, 500, 500), GameObj('болото.png', 1500, 2500, 500, 500)]"""
        delta = GameObj('null.png', 0, 0, 1, 1)
        GameObj('пустыня.png', 0, -100, 2000, 100, col=True)
        GameObj('пустыня.png', -100, 0, 100, 2000, col=True)
        GameObj('пустыня.png', 0, 2000, 2000, 100, col=True)
        GameObj('пустыня.png', 2000, 0, 100, 2000, col=True)
        tank1 = BaseTank(101, 101, 0, 'tank_body.png', 'A', 16, 100, 3)
        tank2 = BaseTank(1200, 1000, 0, 'tank_body.png', 'B', 16, 100, 3)
        tank3 = BaseTank(1500, 1500, 0, 'tank_body.png', 'B', 16, 100, 3)
        track11 = Track('track1.png', 'track2.png', "A", tank1, 8, 0)
        track12 = Track('track1.png', 'track2.png', "A", tank1, 8, 180)
        track21 = Track('track1.png', 'track2.png', "B", tank2, 8, 0)
        track22 = Track('track1.png', 'track2.png', "B", tank2, 8, 180)
        track31 = Track('track1.png', 'track2.png', "B", tank3, 8, 0)
        track32 = Track('track1.png', 'track2.png', "B", tank3, 8, 180)
        ai1 = Aim("A")
        ai2 = Aim("B", is_ai=True, aim=True)
        ai4 = Aim("B", is_ai=True, aim=True)
        ai3 = Aim('B', is_ai=True, aim=False)
        ai5 = Aim('B', is_ai=True, aim=False)
        tank2.aim = ai3
        tank3.aim = ai5
        gun1 = TankGun('gun1.png', "A", tank1, ai1, 8)
        gun2 = TankGun('gun1.png', "B", tank2, ai2, 8)
        gun3 = TankGun('gun1.png', "B", tank3, ai4, 8)
        camera = Camera()
        ai11 = AI(maapai, ai3, gun2, tank2)
        ai12 = AI(maapai, ai5, gun3, tank3)
        ai3.ai = ai11
        ai5.ai = ai12
        running = True
        player = tank1
        m1 = False
        m2 = False
        k2 = 1
        k3 = 1
        mousepos = (0, 0)
        sound_battle.play(-1)
        t = Textrender(screen, screen_resolution=w / 800)
        tmf = 0
        while running:
            print(tank2.xp, tank3.xp)
            ai12.update()
            ai11.update()
            cur_fps = clock.get_fps()
            timer += 0.01
            k = player.maxspeed / abs(player.crspeed if player.crspeed != 0 else 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sound_battle.stop()
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
                if event.type == pygame.MOUSEBUTTONDOWN and tmf <= timer:
                    gun1.fire()
                    tmf = timer + 3
                player.givekf(m1, m2, k, k2, k3)
            screen.fill((100, 100, 100))
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
    MainGame(1040, 780, [1], 0)
