"""
Group A: Breakout Game
Contributor: Luis Orellana

Description:
The following class initializes the brick grid component.
It contains a method to render the brick grid to the screen.
It contains a method to check if all brick have been destroyed.

"""
import pygame
from brick import Brick


class BrickGrid:
    # Class variables
    ROWS = 4
    PADDING = 3  # Space between each brick
    COLORS = ["red", "green", "orange", "blue"]

    # Constructor
    def __init__(self, screen_width):
        self.bricks_array = []
        self.add_bricks(screen_width)

    # Add bricks to array
    def add_bricks(self, screen_width):
        # Determines the amount of columns needed based on the screen width provided
        columns = int((screen_width / (Brick.WIDTH + self.PADDING)))
        # Ensures brick grids are aligned to screen
        brick_offset = (
            screen_width - (columns * (Brick.WIDTH + self.PADDING))) // 2  # floor division
        for row in range(self.ROWS):
            color = self.COLORS[row]
            for column in range(columns):
                x = brick_offset + column * (Brick.WIDTH + self.PADDING)
                y = row * (Brick.HEIGHT + self.PADDING)
                self.bricks_array.append(Brick(x, y, color))

    # Iterates through the bricks_array and creates brick grid
    def draw(self, screen):
        for brick in self.bricks_array:
            if brick.active:
                brick.draw(screen)

    def update(self):
        pass  # No logic as of now

    def all_bricks_destroyed(self):
        for brick in self.bricks_array:
            if brick.active:
                return False
        return True
