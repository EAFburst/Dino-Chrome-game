import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_run1 = pygame.image.load("assets/images/dinorun1.png")
        self.image_run2 = pygame.image.load("assets/images/dinorun2.png")
        self.image = self.image_run1
    def update(self):
        if self.image == self.image_run1:
            self.image = self.image_run2
        else:
            self.image = self.image_run1
        
