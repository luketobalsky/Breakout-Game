"""
Group A: Breakout Game
Contributor: Lucas Tobalsky

Description:
This module defines the ScoreManager class, which tracks the player's score,
allows points to be added, and resets the score when needed.
"""


from game.settings import Settings


class ScoreManager:
    """
    Manages the player's score throughout the game.

    Provides methods to add points, retrieve the current score,
    and reset the score to its initial value.
    """

    def __init__(self):
        """
        Initializes the score manager with the starting score
        defined in Settings.
        """
        self.score = Settings.INITIAL_SCORE.value

    def add(self, points):
        """
        Adds the given number of points to the player's score.

        Parameters:
            points (int): The number of points to add.
        """
        self.score += points

    def current_score(self):
        """
        Returns the player's current score.

        Returns:
            int: The current score value.
        """
        return self.score

    def clear(self):
        """
        Resets the player's score back to zero.
        """
        self.score = 0
