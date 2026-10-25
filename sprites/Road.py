from pathlib import Path

import pygame


class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = Path(__file__).resolve().parent.parent / "assets" / "images" / "road.png"
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image1 = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect1 = self.image1.get_rect()
        surface = pygame.display.get_surface()
        self.rect.midleft = surface.get_rect().midleft
        self.rect1.topleft = self.rect.topright

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)

    def update(self):
        self.rect.x -= 5
        self.rect1.x -= 5
        if self.rect.right <= 0:
            self.rect.left = self.rect1.right
        elif self.rect1.right <= 0:
            self.rect1.left = self.rect.right