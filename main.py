import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() # Initialise pygame
    # Initialise screen to given dimensions in a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # Initialise clock for screen
    dt = 0 # Time delta

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2) # Initialise a player in the middle of the screen
    asteroid_field = AsteroidField()

    # Infinite loop to draw game on screen
    while True:
        # Check if the user has closed the window, if so, exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") # Fill the screen with solid black
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game Over!")
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        for item in drawable:    
            item.draw(screen) # Draw the player object on the screen

        pygame.display.flip() # Refresh the screens
        dt = clock.tick(60) / 1000 # Limit framerate to 60 FPS

if __name__ == "__main__":
    main()
