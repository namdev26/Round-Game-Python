import pygame
from os.path import join
import Player.Player as Player
import sprites
from display import WINDOW_HEIGHT, WINDOW_WIDTH
from Maps.ListOfMap.Map1 import map1

pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("DEMO")

player = Player.Player((sprites.all_sprites, sprites.Player_sprites), (25, 200))
player2 = Player.Player((sprites.all_sprites, sprites.Player_sprites), (4 * WINDOW_WIDTH / 5, WINDOW_HEIGHT / 2 + 20))
player2.ammo = 0
player2.max_ammo = 0
run = True 
clock = pygame.time.Clock() 
while run:
    #game end:a
    if len(sprites.Player_sprites) < 2:
        print(__name__(player for player in sprites) + " WIN")
        pygame.time.wait(1000)
        break

    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
            break
    WINDOW.fill("white")
    sprites.all_sprites.update(dt)
    sprites.Bullet_sprites.draw(WINDOW)
    sprites.Player_sprites.draw(WINDOW)
    sprites.Explosion_sprites.draw(WINDOW)
    for surface in map1.list_of_surface:
        pygame.draw.polygon(WINDOW, "gray", surface.list_of_2point)

    pygame.display.update()