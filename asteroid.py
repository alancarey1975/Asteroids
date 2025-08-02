import pygame
import random

from circleshape import CircleShape  # Import base class for circular game objects
from constants import *  # Import constant values like ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Initialize parent class with position and radius
    
    # Draw the asteroid on screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    # Update position of asteroid
    def update(self, dt):
        self.position += self.velocity * dt  # Move asteroid based on velocity and time delta

    def split(self):
        self.kill()  # Remove the current asteroid from all sprite groups
        if self.radius <= ASTEROID_MIN_RADIUS:  # Check if asteroid is too small to split
            return  # Exit if no further splitting is possible
        else:
            random_angle = random.uniform(20, 50)  # Generate a random angle between 20 and 50 degrees
            new_radius = self.radius - ASTEROID_MIN_RADIUS  # Calculate radius for new smaller asteroids

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)  # Create first new asteroid
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)  # Create second new asteroid
            new_asteroid1.velocity = pygame.Vector2.rotate(self.velocity, +random_angle) * 1.2  # Set velocity for first asteroid, rotated and sped up
            new_asteroid2.velocity = pygame.Vector2.rotate(self.velocity, -random_angle) * 1.2  # Set velocity for second asteroid, rotated oppositely and sped up

            
