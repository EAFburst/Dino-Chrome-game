import random
from pathlib import Path

import pygame


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = Path(__file__).resolve().parent.parent / "assets" / "images" / "cloud.png"
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.x = surface.get_width() + random.randint(0, 200)
        self.rect.y = random.randint(0, int(surface.get_height() / 2 - self.rect.height))
        self.num = random.randint(3, 7)

    def update(self):
        self.rect.x -= self.num
        if self.rect.right <= 0:
            self.kill()
