import pygame
from src import tiles
import player
import world
import constants

pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()
time = 0

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((960, 540))
        self.screen.fill(0, 0, 0)   #replace with bg image later
        
        
        