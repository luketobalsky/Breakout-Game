"""
Group A: Breakout Game
Contributor: Luis Orellana

Description:
This module defines the Brick class, which represents a single destructible block
in the brick grid. Bricks have a position, size, color, and active state, and can be drawn
and destroyed during gameplay. It contains a method to render the brick to the screen,and
it contains a method to destroy the brick.
"""

import pygame
from game.components import Components
from game.settings import Settings


class Brick(Components):
    """
    Represents a single brick in the Breakout grid.

    Each brick has a position, size, color, and an active state.
    Bricks can be drawn to the screen and deactivated when hit by the ball.
    """

    # Constructor
    def __init__(self, x, y, color="red"):
        """
        Creates a brick at the given (x, y) position.

        Parameters:
            x (int): Horizontal position of the brick.
            y (int): Vertical position of the brick.
            color (str): Color key used to select the brick's color
            from Settings.BRICK_COLORS.
        """
        super().__init__(x, y, Settings.BRICK_WIDTH.value, Settings.BRICK_HEIGHT.value)
        self.color = Settings.BRICK_COLORS.value[color]
        self.active = True

    # Methods

    def draw(self, screen):
        """
        Draws the brick on the screen if it is active.

        Parameters:
            screen (pygame.Surface): The surface to draw the brick on.
        """
        if self.active:
            pygame.draw.rect(screen, self.color,
                             self.rect, border_radius=2)

    def destroy(self):
        """
        Marks the brick as inactive so it is no longer drawn or collidable.
        """
        self.active = False
