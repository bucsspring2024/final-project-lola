import pygame
import tiles
import pygame.freetype
import player

screen = pygame.display.set_mode((960, 540))
TILE_TYPES = 8
img_list = []
TILE_SIZE = 50
for x in range(TILE_TYPES):
    img = pygame.image.load(f"img/Tiles_000{x+1}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE)) #size down tile image
    img_list.append(img) #add tile image to list
    #each tile is named 0, 1, or 2
#GAME_FONT = pygame.freetype.Font(None,size=48)

class World():
    def __init__(self):
        self.obstacle_list = []
        self.damage_group = pygame.sprite.Group()
        self.decoration_group = pygame.sprite.Group()
        
    def process_data(self, data):
        for y, row in enumerate(data): #y is just the row containing nested list
            for x, tile in enumerate(row): #x is the position of tile in row
                img = img_list[tile]
                #access the image corresponding to index tile, as defined above
                img_rect = img.get_rect()
                img_rect.x = x * TILE_SIZE
                img_rect.y = y * TILE_SIZE
                #img_rect.x retrieves the x coord of the top left corner, we then multiply by tilesize to place in correct spot
                #we place these tiles in the right spot with the conditionals below
                tile_data = [img, img_rect, -100]
                #for each item in the row, make a tuple with the image & its coordinates
                if tile == 0:
                    self.obstacle_list.append(tile_data)
                elif tile == 1:
                    spikes = tiles.Spike(img, (TILE_SIZE, TILE_SIZE), img_rect.x, img_rect.y)
                    self.damage_group.add(spikes)

    def draw(self, move, dt):
        #print(self.obstacle_list[0][1].x)
        if move == 1 and self.obstacle_list[0][1].x < 450:
            dx = 5
            for sprite in self.damage_group:
                if sprite.rect.x < 0 and sprite.rect.x + dx > 0:
                    sprite.rect.x = 0
                sprite.rect.x += dx
            for tile in self.obstacle_list:
                if tile[1].x < 0 and tile[1].x + dx > 0:
                    tile[1].x = 0
                tile[1].x += dx
        if move == -1:
            dx = -5
            for sprite in self.damage_group:
                if sprite.rect.x > 0 and sprite.rect.x + dx < 0:
                    sprite.rect.x = 0
                sprite.rect.x += dx
            for sprite in self.decoration_group:
                if sprite.rect.x > 0 and sprite.rect.x + dx < 0:
                    sprite.rect.x = 0
                sprite.rect.x += dx
            for tile in self.obstacle_list:
                if tile[1].x > 0 and tile[1].x + dx < 0:
                    tile[1].x = 0
                tile[1].x += dx
        for tile in self.obstacle_list:
            screen.blit(tile[0],tile[1])
        self.damage_group.update()
        self.damage_group.draw(screen)
        self.decoration_group.draw(screen)
