"""
Group A: Breakout Game
Contributor: Baba Diawara

Description:
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
"""

import pygame

from game.components import Components
from game.settings import Settings
from game.paddle import Paddle
from game.brick import Brick


class Ball(Components):
    """
    The Ball class interacts closely with:
    - Settings: for screen dimensions and direction constants.
    - Paddle: to detect paddle hits and bounce vertically.
    - Brick: to detect brick hits and determine bounce direction.

    This module is part of the core gameplay mechanics and is used by
    the main game loop to update and draw the ball each rect.
    """

    def __init__(self):
        super().__init__(Settings.BALL_X.value, Settings.BALL_Y.value,
                         Settings.BALL_WIDTH.value, Settings.BALL_HEIGHT.value)

        # Movement speed
        self.speed_x = Settings.BALL_SPEED_X.value
        self.speed_y = Settings.BALL_SPEED_Y.value

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
        # Apply movement
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off left or right walls and ensures the ball does not exceed the boundaries
        if self.rect.left < 0:
            self.rect.left = 0
            self.bounce(Settings.HORIZONTAL)
        elif self.rect.right > Settings.SCREEN_WIDTH.value:
            self.rect.right = Settings.SCREEN_WIDTH.value
            self.bounce(Settings.HORIZONTAL)

        # Bounce off top wall
        if self.rect.top < 0:
            self.rect.top = 0
            self.bounce(Settings.VERTICAL)

        # Ball fell below the screen → game over
        if self.rect.bottom > Settings.SCREEN_HEIGHT.value:
            self.game_over = -1

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

    def draw(self, screen):
        """
        Draws the ball on the screen.
        """
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (self.rect.x + Settings.RADIUS.value,
             self.rect.y + Settings.RADIUS.value),
            Settings.RADIUS.value
        )

    def bounce_direction(self, paddle):
        self.rect.bottom = paddle.rect.top

        #find location of ball compared to the paddle and 
        center = self.rect.centerx
        paddle_center = paddle.rect.centerx
        offset = center - paddle_center
        intersect = offset / (paddle.width / 2)
        speed = max(abs(self.speed_y), 4)
        self.speed_x = int(intersect * speed)

        if abs(self.speed_x) < 2:
            self.speed_x = 2 if intersect >= 0 else -2

        self.speed_y = -speed


    # May need to be deleted.
    def update(self):
        pass

