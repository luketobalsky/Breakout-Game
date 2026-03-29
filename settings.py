# This will be the settings file to store all universal settings for the game

# Add settings into here and then import any used settings in other files with the import line
from enum import Enum


class Settings(Enum):
    # The following are used to determine the ball bouncing Axis
    HORIZONTAL = 1
    VERTICAL = 2

    SCREEN_X = 600
    SCREEN_Y = 600
