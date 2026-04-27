"""
Group A: Breakout Game
Contributor: Baba Diawara

Description:
The following module defines the Settings enum, which stores all configuration constants
used throughout the game, including screen dimensions, ball settings,
paddle settings, brick settings, difficulty scaling, and scoring rules.

Using an Enum ensures all settings are centralized, immutable, and
accessed consistently across the project.
"""


from enum import Enum


class Settings(Enum):
    """
    Collection of global configuration constants for the Breakout game.

    Values include screen dimensions, object sizes, speeds, colors,
    difficulty parameters, and scoring defaults. Access values using
    Settings.NAME.value.
    """

    # Bounce axis identifiers
    HORIZONTAL = 1
    VERTICAL = 2

    # Collision sides
    TOP = 1111
    BOTTOM = 1112
    LEFT = 1113
    RIGHT = 1114

    # Screen dimensions
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    # Ball settings
    RADIUS = 10
    BALL_X = SCREEN_WIDTH // 2 - RADIUS
    BALL_Y = SCREEN_HEIGHT // 2
    BALL_WIDTH = RADIUS * 2
    BALL_HEIGHT = RADIUS * 2
    COLLISION_THRESHOLD = 12
    BALL_SPEED_X = 4
    BALL_SPEED_Y = -4

    # Paddle settings
    PADDLE_X = SCREEN_WIDTH // 2
    PADDLE_Y = SCREEN_HEIGHT - 50
    PADDLE_WIDTH = 100
    PADDLE_HEIGHT = 15
    PADDLE_SPEED = 10

    # Brick settings
    BRICK_WIDTH = 42
    BRICK_HEIGHT = 14
    BRICK_COLORS = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "orange": (255, 165, 0),
        "blue": (0, 0, 255),
    }

    # BrickGrid settings
    GRID_ROWS = 4
    GRID_PADDING = 3  # Space between each brick
    GRID_COLORS = ["red", "green", "orange", "blue"]

    # Lives settings
    LIVES = 3

    # Difficulty settings
    SPEED_INCREMENT = 2
    MAX_LEVEL = 3

    # Score and Level settings
    INITIAL_SCORE = 0
    INITIAL_LEVEL = 1

    # Game settings
    FRAMES = 60  # Game speed in frames per second
