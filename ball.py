"""
ball.py

This module defines the Ball class used in the breakout-style game.
The Ball is responsible for handling its own movement, detecting
collisions with game objects (such as the Paddle and Bricks), and
responding to those collisions by bouncing appropriately.

Key Responsibilities:
- Maintain the ball's position, velocity, and bounding rectangle.
- Move the ball each rect and detect screen boundary collisions.
- Detect collisions with Paddle and Brick objects using pygame.Rect.
- Reverse velocity along the correct axis when a collision occurs.
- Report game-over conditions when the ball falls below the screen.
- Render the ball onto the game window.

The Ball class interacts closely with:
- Settings: for screen dimensions and direction constants.
- Paddle: to detect paddle hits and bounce vertically.
- Brick: to detect brick hits and determine bounce direction.

This module is part of the core gameplay mechanics and is used by
the main game loop to update and draw the ball each rect.
"""
# Contributor: Baba Diawara

import pygame
from pygame import Rect

from components import Components
from settings import Settings
from paddle import Paddle
from brick import Brick


class Ball(Components):
    
    def __init__(self, x, y):
        super().__init__(x - Settings.RADIUS.value, y,
                         Settings.RADIUS.value * 2, Settings.RADIUS.value * 2)

        # Pygame Rect used for movement & collision detection
        self.rect = Rect(self.x, self.y, self.width, self.height)

        # Movement speed
        self.speed_x = 4
        self.speed_y = -4
        # Game state
        self.game_over = 0
        # The side of the item the ball has hit
        self.collision_side = None

    def move(self):
        """
        Moves the ball and handles screen boundary collisions.
        Returns:
            -1 if ball falls below screen (game over)
             0 otherwise
        """

        # Bounce off left or right walls
        if self.rect.left < 0 or self.rect.right > Settings.SCREEN_X.value:
            self.bounce(Settings.HORIZONTAL)

        # Bounce off top wall
        if self.rect.top < 0:
            self.bounce(Settings.VERTICAL)

        # Ball fell below the screen → game over
        if self.rect.bottom > Settings.SCREEN_Y.value:
            self.game_over = -1

        # Apply movement
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over

    def bounce(self, axis: Settings):
        """
        Reverses velocity depending on collision axis.
        """
        match axis:
            case Settings.VERTICAL:
                self.speed_y *= -1
            case Settings.HORIZONTAL:
                self.speed_x *= -1

    def has_hit(self, item: Components):
        """
        Detects collisions with Paddle or Brick.
        Returns True if a collision occurred.
        """

        # Paddle collision
        if isinstance(item, Paddle):
            if self.rect.colliderect(item.rect):

                # Ball hits top of paddle while moving downward
                if abs(self.rect.bottom - item.rect.top) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_y > 0:
                    self.collision_side = Settings.TOP
                    return True

        # Brick collision
        elif isinstance(item, Brick):
            if self.rect.colliderect(item.rect):

                # --- Vertical collisions ---
                if abs(self.rect.bottom - item.rect.top) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_y > 0:
                    self.collision_side = Settings.TOP
                    return True

                if abs(self.rect.top - item.rect.bottom) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_y < 0:
                    self.collision_side = Settings.BOTTOM
                    return True

                # --- Horizontal collisions ---
                if abs(self.rect.right - item.rect.left) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_x > 0:
                    self.collision_side = Settings.LEFT
                    return True

                if abs(self.rect.left - item.rect.right) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_x < 0:
                    self.collision_side = Settings.RIGHT
                    return True

        return False  # No collision

    def draw(self, screen, colour):
        """
        Draws the ball on the screen.
        """
        pygame.draw.circle(
            screen,
            colour,
            (self.rect.x + Settings.RADIUS.value, self.rect.y + Settings.RADIUS.value),
            Settings.RADIUS.value
        )

    # May need to be deleted.
    def update(self):
        pass
