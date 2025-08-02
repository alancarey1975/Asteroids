import pygame
import sys

from constants import *  # Import constant values like SCREEN_WIDTH and SCREEN_HEIGHT
from player import Player  # Import Player class for the player's ship
from asteroid import Asteroid  # Import Asteroid class for individual asteroids
from asteroidfield import AsteroidField  # Import AsteroidField class for spawning asteroids
from shot import Shot  # Import Shot class for player-fired projectiles

def main():
    pygame.init()  # Initialize pygame and its modules
    # Create a display window with dimensions defined in constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Create a clock object to control frame rate
    dt = 0  # Delta time (in seconds) for frame-rate-independent updates

    # Create sprite groups to manage different types of game objects
    updatable = pygame.sprite.Group()  # Group for objects that need updating
    drawable = pygame.sprite.Group()  # Group for objects that need drawing
    asteroids = pygame.sprite.Group()  # Group for all asteroid objects
    shots = pygame.sprite.Group()  # Group for all shot (projectile) objects

    # Assign sprite groups as containers for each class to automatically add instances
    Player.containers = (updatable, drawable)  # Player belongs to updatable and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)  # Asteroids belong to their own group plus updatable and drawable
    AsteroidField.containers = (updatable)  # AsteroidField only needs updating, not drawing
    Shot.containers = (shots, updatable, drawable)  # Shots belong to their own group plus updatable and drawable

    # Create a player object positioned at the center of the screen
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  # Create an asteroid field to spawn asteroids

    # Main game loop that runs until the game ends
    while True:
        # Process all events (e.g., keyboard, mouse, window events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window
                return  # Exit the game loop and end the program

        screen.fill("black")  # Clear the screen by filling it with black
        updatable.update(dt)  # Update all objects in the updatable group (e.g., move player, asteroids, shots)

        # Check for collisions between asteroids and player or shots
        for asteroid in asteroids:
            if asteroid.collision(player):  # If an asteroid collides with the player
                sys.exit("Game Over!")  # End the game with a "Game Over" message
            for shot in shots:  # Check each shot against each asteroid
                if asteroid.collision(shot):  # If a shot hits an asteroid
                    shot.kill()  # Remove the shot from all groups
                    asteroid.split()  # Split or destroy the asteroid (defined in Asteroid class)

        # Draw all drawable objects (player, asteroids, shots) to the screen
        for item in drawable:
            item.draw(screen)  # Call the draw method of each object to render it

        pygame.display.flip()  # Update the display to show the new frame
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and calculate delta time in seconds

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly