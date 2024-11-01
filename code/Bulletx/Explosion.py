import os.path
import sys
import pygame

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from display import WINDOW_HEIGHT, WINDOW_WIDTH
import sprites
from Maps.ListOfMap.Map1 import map1

def Explode(bullet, dt):
    if pygame.time.get_ticks() - bullet.time_collided > 1500:
        bullet.kill()
        Explosion(sprites.Explosion_sprites, bullet.rect.center)
    elif pygame.time.get_ticks() - bullet.time_collided > 5:
        bullet.direction.xy = (0, 0)
        bullet.gravity = 0

class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__((groups, sprites.all_sprites))
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_frect(center = pos)
        self.duration = 100
        self.time = pygame.time.get_ticks()
    def update(self, dt):
        current = pygame.time.get_ticks()
        if current - self.time > self.duration :
            self.kill()