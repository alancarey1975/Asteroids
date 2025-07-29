import pygame

from constants import *
from player import Player

def main():
    pygame.init() # Initialise pygame
    # Initialise screen to given dimensions in a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # Initialise clock for screen
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2) # Initialise a player in the middle of the screen

    # Infinite loop to draw game on screen
    while True:
        # Check if the user has closed the window, if so, exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") # Fill the screen with solid black
        player.draw(screen) # Draw the player object on the screen
        pygame.display.flip() # Refresh the screen
        dt = clock.tick(60) / 1000 # Limit framerate to 60 FPS

if __name__ == "__main__":
    main()
