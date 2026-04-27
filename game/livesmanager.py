"""
Group A: Breakout Game
Contributor: Lucas Tobalsky

Description:
This module defines the LivesManager class, which tracks the player's remaining lives,
handles life loss, and resets lives when starting a new game.
"""

from game.settings import Settings


class LivesManager:
    """
    Manages the player's remaining lives.

    Provides methods to decrement lives when the player loses the ball,
    retrieve the current number of lives, and reset lives to the starting
    amount defined in Settings.
    """

    def __init__(self):
        """
        Initializes the lives manager with the starting number of lives
        defined in Settings.
        """
        self.lives = Settings.LIVES.value

    def lose_life(self):
        """
        Decreases the player's life count by one, if any lives remain.
        """
        if self.lives > 0:
            self.lives -= 1

    def current_lives(self):
        """
        Returns the number of lives the player currently has.

        Returns:
            int: The current life count.
        """
        return self.lives

    def clear(self):
        """
        Resets the player's lives back to the starting amount.
        """
        self.lives = Settings.LIVES.value
