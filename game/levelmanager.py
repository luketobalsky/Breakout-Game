"""
Group A: Breakout Game
Contributor: Luis Orellana

Description:
This module defines the LevelManager class, which tracks the player's current level,
increments levels as the player progresses, and resets levels when a new
game begins.
"""

from game.settings import Settings


class LevelManager:
    """
    Manages the current level of the game.

    Tracks the active level, provides methods to increment or reset it,
    and exposes the current level value for use by other systems such as
    difficulty scaling and UI rendering.
    """

    def __init__(self):
        """
        Initializes the level manager using the starting level defined
        in Settings.
        """
        self.level = Settings.INITIAL_LEVEL.value

    def increment_level(self):
        """
        Advances the game to the next level.
        """
        self.level += 1

    def reset_levels(self):
        """
        Resets the level back to the starting value.
        """
        self.level = 1

    def get_level(self):
        """
        Returns the current level number.

        Returns:
            int: The current game level.
        """
        return self.level
