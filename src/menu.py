import pygame
import pygame.freetype
from src.constants import Constants

pygame.init()
pygame.freetype.init()
constant = Constants()

screen = pygame.display.set_mode((960, 540))  # Set your desired screen size
clock = pygame.time.Clock()  # Create a clock object to control frame rate

class Menu():
    def __init__(self):
        self.start_game = False
        self.quit = False
        self.font = constant.GAME_FONT
        self.text_color = (255, 255, 255)
        self.texts = ["Start Game", "Quit"]
        self.rects = [pygame.Rect(300, 255, 200, 50), pygame.Rect(300, 350, 200, 50)]
        
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(self.rects):
                    if rect.collidepoint(event.pos):
                        if i == 0:
                            self.start_game = True
                        elif i == 1:
                            self.quit = True
    def draw(self, screen):
        screen.fill((0, 0, 0))
        for i, text in enumerate(self.texts):
            pygame.draw.rect(screen, (100, 100, 100), self.rects[i]) #draw button rectangle
            text_surface, rect = self.font.render(text, self.text_color)
            screen.blit(text_surface, self.rects[i])

        
        
        
        
# #Testing things
# menu = Menu()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Update the menu based on events
#     menu.update(pygame.event.get())

#     # Draw the menu
#     screen.fill((0, 0, 0))  # Clear the screen with black
#     menu.draw(screen)  # Draw the menu on the screen

#     pygame.display.flip()  # Update the display
#     clock.tick(60)  # Cap the frame rate at 60 FPS

# pygame.quit()  # Quit Pygame


