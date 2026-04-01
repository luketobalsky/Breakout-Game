from enum import Enum


class Settings(Enum):
    """
    Global game configuration values used throughout the project.

    This Enum stores:
    - Axis identifiers for ball bounce logic
    - Ball-related constants (radius, collision threshold)
    - Screen dimensions

    All values are accessed using Settings.NAME.value
    """

    # Bounce axis identifiers
    HORIZONTAL = 1
    VERTICAL = 2

    # Collision sides
    TOP = 1111
    BOTTOM = 1112
    LEFT = 1113
    RIGHT = 1114

    # Ball properties
    COLLISION_THRESHOLD = 5
    RADIUS = 10

    # Screen dimensions
    SCREEN_X = 1000
    SCREEN_Y = 600

    #Lives 
    LIVES = 3

    #Game Speed (Frames)
    FRAMES = 60
