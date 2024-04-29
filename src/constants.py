import pygame
import pygame.freetype

class Constants:
    pygame.init()
    pygame.freetype.init()
        
    GAME_FONT = pygame.freetype.Font(r'assets/8-BIT WONDER.TTF', size = 30)
    SCREEN_SIZE = pygame.display.set_mode((960, 540))

# # TESTING
# constants = Constants()      
# # Render text using the custom font
# text = "Hello, World!"
# text_surface, rect = constants.GAME_FONT.render(text, (255, 255, 255))  # Render text with white color
# screen = pygame.display.set_mode((800, 600))  # Create the game screen
# screen.fill((0, 0, 0))  # Clear the screen (fill with black)

# # Blit the text surface onto the screen
# screen.blit(text_surface, (100, 100))  # Specify the position (x, y) for the text
# pygame.display.flip()  # Update the display

# # Main loop to handle events
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # Quit Pygame
# pygame.quit()
