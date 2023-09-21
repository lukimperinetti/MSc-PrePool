import pygame
import pytmx
import pyscroll
from player import Player

pygame.init()


class Game:
    def __init__(self):
        # Create the game screen
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("The Hangman Game")

        # Load the map
        tmx_data = pytmx.util_pygame.load_pygame("/home/lukimperinetti/Documents/MSc-PrePool/Day09/map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())


        #generate the player
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)


        # draw the map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

    
    def run(self):
        # Game loop
        runing = True
        while runing:
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get(): # Get all the events
                if event.type == pygame.QUIT: # If the event is quit
                    runing = False
        pygame.quit() # Quit the game