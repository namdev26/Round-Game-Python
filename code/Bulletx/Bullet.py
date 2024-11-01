import pygame
import math
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from display import WINDOW_HEIGHT as y
from display import WINDOW_WIDTH as x
import sprites
from Maps.ListOfMap.Map1 import map1
from Bulletx.Explosion import Explode

class Bullet(pygame.sprite.Sprite):
    def __init__(self,groups, pos, angle, homing, explode, player, speed, size, gravity, slow, bounce_time, dmg):
        super().__init__(groups)
        self.radius = size
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.rect = self.image.get_frect(center = pos)
        self.speed = speed
        self.direction = pygame.math.Vector2(self.speed * math.cos(angle), self.speed * math.sin(angle))
        self.time_appeared = pygame.time.get_ticks()
        self.dmg = dmg

        #homing stats
        self.homing = homing
        self.angle_vel = 180
        self.maxspeed_vel_homing = 2000
        self.speed_acc_homing = 1000

        #Gravity
        self.gravity = gravity

        #shooter
        self.player = player
        self.hit_able = False

        #Explode
        self.explode = explode
        self.collided = False
        self.time_collided = 0

        #Bounce
        self.bounce_time = bounce_time

        #slow on hit
        self.slow = slow
    def Bouncing(self, dt):
        #Bouncing
        wall = [(0, 0), (x, 0), (x, y), (0, y), (0, 0)]
        rect_temp = self.image.get_frect(center = self.rect.center + self.direction * dt)
        for index in range((len(wall)) - 1):
            if rect_temp.clipline(wall[index], wall[index + 1]):
                if self.bounce_time > 0:
                    point1 = pygame.math.Vector2(wall[index][0], wall[index][1])
                    point2 = pygame.math.Vector2(wall[index + 1][0], wall[index + 1][1])
                    pos = pygame.math.Vector2(self.rect.center)
                    self.direction = self.Bounce(point1, point2, pos, self.direction)
                    self.bounce_time -= 1
                else:
                    self.kill()
        bounced = False
        if not self.collided:
            for surface in map1.list_of_surface:
                for index in range(len(surface.list_of_2point) - 1):
                    if rect_temp.clipline(surface.list_of_2point[index], surface.list_of_2point[index + 1]):
                        if self.bounce_time > 0 and self.explode == False:
                            point1 = pygame.math.Vector2(surface.list_of_2point[index][0], surface.list_of_2point[index][1])
                            point2 = pygame.math.Vector2(surface.list_of_2point[index + 1][0], surface.list_of_2point[index + 1][1])
                            pos = pygame.math.Vector2(self.rect.center)
                            self.direction = self.Bounce(point1, point2, pos, self.direction)
                            bounced = True
                        elif self.explode:
                            self.time_collided = pygame.time.get_ticks()
                            self.collided = True
                        else:
                            self.kill()
        else:
            Explode(self, dt)
                        
        if bounced:
            self.bounce_time -= 1

    #Bounce from line
    def Bounce(self, lp0, lp1, pt, dir):
        l_dir = (lp1 - lp0).normalize()  #vector canh tam giac
        nv = pygame.math.Vector2(-l_dir[1], l_dir[0]) #vector phap tuyen tren
        d = (lp0 - pt).dot(nv)  #khoang cach giữa bong voi canh tam giac
        ptX = pt + nv * d  # tim giao diem
        r_dir = dir.reflect(nv)  # reflect the direction vector on the line
        return r_dir
    
    #Homing
    def Homing(self, dt):
        founded = False         #tim thay player
        not_collided = True     #co the nhin thay player (không bị cản bởi tường)
        Min = 1e9
        choosen_angle = 0

        #check co the nhin thay player
        if self.hit_able:
            for another_player in sprites.Player_sprites:
                for surface in map1.list_of_surface:
                    for index in range(len(surface.list_of_2point) - 1):
                        point1 = pygame.math.Vector2(surface.list_of_2point[index][0], surface.list_of_2point[index][1])
                        point2 = pygame.math.Vector2(surface.list_of_2point[index + 1][0], surface.list_of_2point[index + 1][1])
                        pt = pygame.math.Vector2(self.rect.center)
                        pt2 = pygame.math.Vector2(another_player.rect.center)
                        if not self.checkLineCollide(point1, point2, pt, pt2):
                            angle = -pygame.math.Vector2(another_player.rect.centerx - self.rect.centerx, another_player.rect.centery - self.rect.centery).angle_to(self.direction)
                            if abs(angle) < 50 and self.homing :
                                length = pygame.math.Vector2(self.player.rect.centerx - another_player.rect.centerx, self.player.rect.centery - another_player.rect.centery).length()
                                if Min > length:
                                    Min = length
                                    choosen_angle = angle
                                founded = True
                # check góc hướng tới
                
        if founded:
            self.direction = self.direction.rotate(min(choosen_angle, self.angle_vel * dt)) if choosen_angle > 0 else self.direction.rotate(max(choosen_angle, -self.angle_vel * dt))
            self.direction.scale_to_length(min(self.direction.length() + self.speed_acc_homing * dt, self.maxspeed_vel_homing))
        else:
            self.direction.y += self.gravity * dt       #(rơi tự do nếu không Homing)

    #Find if 2 line is collided (kiểm tra vector đạn -> người chơi có bị chặn bởi tường không)
    def checkLineCollide(self, lp0, lp1, pt, pt2):
        dir = pygame.math.Vector2(pt2 - pt)
        l_dir = (lp1 - lp0).normalize()
        nv = pygame.math.Vector2(-l_dir[1], l_dir[0])
        d1 = (lp0 - pt).dot(nv)
        d2 = (lp0 - pt2).dot(nv)
        if(d1 * d2 < 0):
            ptX1 = pt + nv * d1
            ptX2 = pt2 + nv * d2
            d1 = abs(d1)
            d2 = abs(d2)
            ptX = (ptX2 - ptX1) * d1 / (d1 + d2) + ptX1
            if ptX.distance_to(lp0) < lp0.distance_to(lp1) and ptX.distance_to(lp1) < lp0.distance_to(lp1):
                return True
            else:
                return False
        else:
            return False
    
    #hit player
    def hit_player(self):
        for player in sprites.Player_sprites:
            dist = pygame.math.Vector2(self.rect.centerx - player.rect.centerx, self.rect.centery - player.rect.centery).length()
            if player == self.player and dist >= (y / 48):
                self.hit_able = True
            if dist < (y / 48) and self.hit_able:
                player.health -= self.dmg
                self.kill()
    
    def update(self, dt):
        self.Bouncing(dt)
        self.Homing(dt)
        self.hit_player()
        self.rect.center += self.direction * dt