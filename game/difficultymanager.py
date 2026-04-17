"""
Group A: Breakout Game
Contributor: Lucas Tobalsky

Description:
This module defines the DifficultyManager class, which adjusts ball speed as the
player progresses through levels and determines when the final level
has been reached.
"""

from game.settings import Settings


class DifficultyManager:
    """
    Manages difficulty scaling throughout the game.

    Controls how the ball's speed increases each level and provides
    logic to determine when the player has reached the final level.
    """

    def __init__(self):
        """
        Initializes difficulty settings using values from Settings.

        Attributes:
            base_speed (int): Starting horizontal ball speed.
            speed_increment (int): Speed increase applied per level.
            max_level (int): Highest level before the game is considered won.
        """
        self.base_speed = Settings.BALL_SPEED_X.value
        self.speed_increment = Settings.SPEED_INCREMENT.value
        self.max_level = Settings.MAX_LEVEL.value

    def increase_difficulty(self, ball, level):
        """
        Increases the ball's speed based on the current level.

        Parameters:
            ball (Ball): The ball object whose speed will be modified.
            level (int): The current game level.
        """
        speed = self.base_speed + (level - 1) * self.speed_increment
        ball.speed_x = speed
        ball.speed_y = -speed

    def final_level(self, level):
        """
        Returns True if the given level exceeds the maximum level.

        Parameters:
            level (int): The current game level.

        Returns:
            bool: True if the player has passed the final level.
        """
        return level > self.max_level
