"""
Group A: Breakout Game

Contributor: Luis Orellana

Description:
This will be the leves manager class which will track the current level

"""

class LevelManager:

    def __init__(self):
        self.level = 1

    def increment_level(self):
        self.level += 1

    def reset_levels(self):
        self.level = 1

    def get_level(self):
        return self.level