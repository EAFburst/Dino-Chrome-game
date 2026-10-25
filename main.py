from sprites.Road import Road
from sprites.cloud import Cloud
import pygame
import sys
from sprites.dino import Dino

pygame.init()

# Constants
WIDTH = 500
HEIGHT = 500
FPS = 60

# Creating a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()

# Sprites
player = Dino()   
road = Road()
clouds = pygame.sprite.Group()
running = True
while running:
    # Screen refresh rate
    clock.tick(FPS)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if len(clouds) < 3:
        clouds.add(Cloud())

    road.update()
    clouds.update()

    # Rendering
    screen.fill((255, 255, 255))
    road.draw(screen)
    clouds.draw(screen)
    player.update(screen)
    pygame.display.update()
