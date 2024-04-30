import pygame
import pygame.freetype
from src.menu import Menu
from src.constants import Constants
from src.game import Game

pygame.init()
pygame.freetype.init()

BG_COLOR = (50, 50, 50) #Replace with bg img later
GAME_FONT = pygame.freetype.Font(None, size = 30)



class Controller:
  
  def __init__(self):
    """
    Setup pygame data.
    """
    self.screen = pygame.display.set_mode((960, 540))
    self.width, self.height = pygame.display.get_window_size()
    pygame.display.set_caption("Soul Finder")
    
    self.background = pygame.Surface((self.width, self.height))
    self.background_color = BG_COLOR
    self.background.fill(self.background_color)
    self.clock = pygame.time.Clock()
    self.state = "menu" #start with menu screen
    self.menu = Menu()
    
  def mainloop(self):
    """
    Select state loop.
    """
    while(True):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      
      if self.state == "menu":
        self.menuloop()
      elif self.state == "game":
        self.gameloop()
      elif self.state == "gameover":
        self.gameoverloop()
        
      pygame.display.flip()

  def menuloop(self):
    """
    Creates a menu to start and quit game.
    """
      #event loop
    menu = Menu()
    while self.state == "menu":
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      
      # Update the menu based on events
      self.menu.update(events)

      # Draw the menu
      self.screen.fill(BG_COLOR)
      self.menu.draw(self.screen)
      pygame.display.flip()

      # Check for menu actions
      if self.menu.start_game == True:
          self.state = "game"  # Transition to game state
      elif self.menu.quit == True:
          pygame.quit()
          exit()
      pygame.display.update()
      

  def gameloop(self, screen):
      #event loop
    game = Game()
    screen.blit()
    while self.state == "game":
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      #update data
      

      #redraw
      self.screen.fill(BG_COLOR)
    
  # def gameoverloop(self):
  #     #event loop

  #     #update data

  #     #redraw
