"""
Group A: Breakout Game
Contributor: Luis Orellana

Description:
The following class initializes the brick component.
It contains a method to render the brick to the screeen 
and it contains a method to destroy the brick.


"""
import pygame
from components import Components


class Brick(Components):
    # Class variables
    WIDTH = 42
    HEIGHT = 14

    COLORS = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "orange": (255, 165, 0),
        "blue": (0, 0, 255),

    }

    # Constructor
    def __init__(self, x, y, color="red"):
        super().__init__(x, y, Brick.WIDTH, Brick.HEIGHT)
        self.color = self.COLORS[color]
        self.active = True
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

    # Methods

    def draw(self, screen):
        # Only draws if brick is active
        if self.active:
            pygame.draw.rect(screen, self.color,
                             self.rect, border_radius=2)

    def update(self):
        pass  # No logic as of now

    def destroy(self):
        self.active = False
