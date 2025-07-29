import pygame

from constants import *

def main():
    # Initialise pygame
    pygame.init()
    # Initialise screen to given dimensions in a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Infinite loop to draw game on screen
    while True:
        # Check if the user has closed the window, if so, exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") # Fill the screen with solid black
        pygame.display.flip() # Refresh the screen

if __name__ == "__main__":
    main()
