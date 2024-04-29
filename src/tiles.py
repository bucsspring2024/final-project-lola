#File with different block types and behaviors
import pygame
class Tiles(pygame.sprite.Sprite):
    def __init__(self, img, size, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.TILE_SIZE = size
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + self.TILE_SIZE[0] // 2, y + (self.TILE_SIZE[1] - self.image.get_height()))
        self.rect.h -= 20 #adjusted for collision
        self.rect.w -= 10
        
class Spikes(pygame.sprite.Sprite):
    def __init__(self, img, size, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.TILE_SIZE = size
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + self.TILE_SIZE[0] // 2, y + (self.TILE_SIZE[1] - self.image.get_height()))
        self.rect.h -= 20 
        self.rect.w -= 10