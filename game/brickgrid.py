"""
Group A: Breakout Game
Contributor: Luis Orellana

Description:
This module defines the BrickGrid class, which manages a collection of Brick
objects arranged in rows and columns, and provides utilities for
drawing the grid and checking if all bricks are destroyed.

"""

from game.brick import Brick
from game.settings import Settings


class BrickGrid:
    """
    Manages a grid of bricks for the Breakout game.

    Responsible for creating the brick layout based on screen width
    and settings, storing all Brick instances, drawing them, and
    checking whether any active bricks remain.
    """

    # Constructor
    def __init__(self):
        """
        Initializes the brick grid and populates it with bricks
        based on the configured screen width and brick settings.
        """
        self.bricks_array = []
        self.add_bricks(Settings.SCREEN_WIDTH.value)

    # Add bricks to array
    def add_bricks(self, screen_width):
        """
        Populates the grid with bricks according to the given screen width.

        Calculates how many columns fit on the screen, centers the grid,
        and creates bricks for each row and column using the configured
        brick size, padding, and row colors.

        Parameters:
        screen_width (int): The width of the game screen in pixels.
        """
        # Determines the amount of columns needed based on the screen width provided
        columns = int((screen_width / (Settings.BRICK_WIDTH.value + Settings.GRID_PADDING.value)))
        # Ensures brick grids are aligned to screen
        brick_offset = (
                               screen_width - (columns * (
                               Settings.BRICK_WIDTH.value +
                               Settings.GRID_PADDING.value))) // 2  # floor division
        for row in range(Settings.GRID_ROWS.value):
            color = Settings.GRID_COLORS.value[row]
            for column in range(columns):
                x = brick_offset + column * (Settings.BRICK_WIDTH.value +
                                             Settings.GRID_PADDING.value)
                y = row * (Settings.BRICK_HEIGHT.value + Settings.GRID_PADDING.value)
                self.bricks_array.append(Brick(x, y, color))

    def all_bricks_destroyed(self):
        """
        Returns True if all bricks in the grid are inactive, otherwise False.
        """
        for brick in self.bricks_array:
            if brick.active:
                return False
        return True

    def draw(self, screen):
        """
        Draws all active bricks in the grid to the given screen.

        Parameters:
        screen (pygame.Surface): The surface to draw the bricks on.
        """
        for brick in self.bricks_array:
            if brick.active:
                brick.draw(screen)
