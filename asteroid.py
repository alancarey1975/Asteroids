import pygame

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # Draw the player on screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    # Capture input keys
    def update(self, dt):
        self.position += self.velocity * dt