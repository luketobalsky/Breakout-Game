"""
ball.py

This module defines the Ball class used in the breakout-style game.
The Ball is responsible for handling its own movement, detecting
collisions with game objects (such as the Paddle and Bricks), and
responding to those collisions by bouncing appropriately.

Key Responsibilities:
- Maintain the ball's position, velocity, and bounding rectangle.
- Move the ball each frame and detect screen boundary collisions.
- Detect collisions with Paddle and Brick objects using pygame.Rect.
- Reverse velocity along the correct axis when a collision occurs.
- Report game-over conditions when the ball falls below the screen.
- Render the ball onto the game window.

The Ball class interacts closely with:
- Settings: for screen dimensions and direction constants.
- Paddle: to detect paddle hits and bounce vertically.
- Brick: to detect brick hits and determine bounce direction.

This module is part of the core gameplay mechanics and is used by
the main game loop to update and draw the ball each frame.
"""
# Contributor: Baba Diawara

from typing import Union

import pygame
from pygame import Rect

from components import Components
from settings import Settings
from paddle import Paddle
from brick import Brick


class Ball(Components):
    class Ball:
        """
        Represents the ball used in the breakout-style game and extends Components.

        The Ball class manages its own position, movement, collision detection,
        and bounce behavior. It uses a pygame.Rect to track its bounding box
        and interacts with other game objects such as the Paddle and Bricks.

        Responsibilities:
        - Maintain the ball's size, position, velocity, and bounding rectangle.
        - Move each frame and detect collisions with screen boundaries.
        - Reverse velocity along the appropriate axis when bouncing.
        - Detect collisions with Paddle and Brick objects and report hits.
        - Signal a game-over condition when the ball falls below the screen.
        - Render itself onto the game window.

        Attributes:
            frame (pygame.Rect): The ball's bounding rectangle.
            speed_x (int): Horizontal movement speed.
            speed_y (int): Vertical movement speed.
            game_over (int): Game state flag (0 = running, -1 = ball lost).
            collision_side (Settings): records the side of the target hit by the ball
        """

    def __init__(self, x, y):
        super().__init__(x - Settings.RADIUS.value, y,
                         Settings.RADIUS.value * 2, Settings.RADIUS.value * 2)

        # Pygame Rect used for movement & collision detection
        self.frame = Rect(self.x, self.y, self.width, self.height)

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
        if self.frame.left < 0 or self.frame.right > Settings.SCREEN_X.value:
            self.bounce(Settings.HORIZONTAL)

        # Bounce off top wall
        if self.frame.top < 0:
            self.bounce(Settings.VERTICAL)

        # Ball fell below the screen → game over
        if self.frame.bottom > Settings.SCREEN_Y.value:
            self.game_over = -1

        # Apply movement
        self.frame.x += self.speed_x
        self.frame.y += self.speed_y

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

    def has_hit(self, item: Union[Brick, Paddle]):
        """
        Detects collisions with Paddle or Brick.
        Returns True if a collision occurred.
        """

        # Paddle collision
        if isinstance(item, Paddle):
            if self.frame.colliderect(item.frame):

                # Ball hits top of paddle while moving downward
                if abs(self.frame.bottom - item.frame.top) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_y > 0:
                    self.collision_side = Settings.TOP
                    return True

        # Brick collision
        elif isinstance(item, Brick):
            if self.frame.colliderect(item.frame):

                # --- Vertical collisions ---
                if abs(self.frame.bottom - item.frame.top) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_y > 0:
                    self.collision_side = Settings.TOP
                    return True

                if abs(self.frame.top - item.frame.bottom) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_y < 0:
                    self.collision_side = Settings.BOTTOM
                    return True

                # --- Horizontal collisions ---
                if abs(self.frame.right - item.frame.left) < Settings.COLLISION_THRESHOLD.value \
                        and self.speed_x > 0:
                    self.collision_side = Settings.LEFT
                    return True

                if abs(self.frame.left - item.frame.right) < Settings.COLLISION_THRESHOLD.value \
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
            (self.frame.x + Settings.RADIUS.value, self.frame.y + Settings.RADIUS.value),
            Settings.RADIUS.value
        )

    def update(self):
        pass
