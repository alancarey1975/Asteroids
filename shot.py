import pygame

from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    # Draw the shot on screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    # Update position of the shot
    def update(self, dt):
        self.position += self.velocity * dt