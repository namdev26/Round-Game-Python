import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pygame
import sprites

class Map(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        # self.image = pygame.Surface((10, 200))
        # self.image.fill("yellow")
        # self.rect = self.image.get_rect(center = (650, 300))
        self.list_of_surface = []