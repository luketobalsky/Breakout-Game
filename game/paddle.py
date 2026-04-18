"""
Group A: Breakout Game
Contributor: Bianca Fouch

Description:
This module defines the Paddle class, which represents the player's controllable
paddle. The paddle can be moved using either keyboard input or mouse
tracking and is responsible for deflecting the ball during gameplay.
"""

import pygame
from game.components import Components
from game.settings import Settings


class Paddle(Components):
    """
    Represents the player's paddle in the Breakout game.

    The paddle can move horizontally using keyboard input or mouse
    tracking. It stays constrained within the screen bounds and is
    responsible for bouncing the ball back into play.
    """

    def __init__(self):
        """
        Initializes the paddle using position and size values from Settings.

        Attributes:
            speed (int): Movement speed of the paddle.
            screen_width (int): Width of the game screen for boundary checks.
            left_pressed (bool): Whether the left movement key is pressed.
            right_pressed (bool): Whether the right movement key is pressed.
            using_mouse (bool): Whether mouse movement controls the paddle.
        """
        super().__init__(
            Settings.PADDLE_X.value,
            Settings.PADDLE_Y.value,
            Settings.PADDLE_WIDTH.value,
            Settings.PADDLE_HEIGHT.value
        )

        self.speed = Settings.PADDLE_SPEED.value
        self.screen_width = Settings.SCREEN_WIDTH.value

        # Input states
        self.left_pressed = False
        self.right_pressed = False

        # Mouse tracking
        self.using_mouse = False

    def move(self):
        """
        Updates the paddle's position based on input.

        - If mouse control is enabled, the paddle follows the mouse's X position.
        - Otherwise, keyboard input (left/right) moves the paddle.
        - Ensures the paddle stays within the screen boundaries.
        """
        if self.using_mouse:
            mouse_x = pygame.mouse.get_pos()[0]
            self.rect.x = mouse_x - self.width // 2
        else:
            if self.left_pressed:
                self.rect.x -= self.speed
            if self.right_pressed:
                self.rect.x += self.speed

        # Keep the paddle within the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + self.width > self.screen_width:
            self.rect.x = self.screen_width - self.width

    def draw(self, screen):
        """
        Draws the paddle on the screen.

        Parameters:
            screen (pygame.Surface): The surface to draw the paddle on.
        """
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
