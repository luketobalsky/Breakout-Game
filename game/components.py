"""
Group A: Breakout Game
Contributor: Luis Orellana

Description:
This module Defines the abstract Components class, which provides shared position,
size, and rectangle attributes for all drawable game objects such as Ball, Paddle, and Brick.
"""

# Abstract Base Class module
from abc import ABC, abstractmethod

from pygame import Rect


class Components(ABC):
    """
    Abstract base class for all game components that have a position,
    size, and drawable representation.

    Provides a pygame.Rect for collision detection and movement, and
    enforces that all subclasses implement a draw() method.
    """

    def __init__(self, x, y, width, height):
        """
        Initializes a component with position and size.

        Parameters:
            x (int): Horizontal position of the component.
            y (int): Vertical position of the component.
            width (int): Width of the component.
            height (int): Height of the component.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Pygame Rect used for movement & collision detection
        self.rect = Rect(self.x, self.y, self.width, self.height)

    @abstractmethod
    def draw(self, screen):
        """
        Draws the component to the screen.

        Must be implemented by subclasses.

        Parameters:
            screen (pygame.Surface): The surface to draw on.
        """
        pass
