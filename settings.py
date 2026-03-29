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

    # Ball properties
    COLLISION_THRESHOLD = 5
    RADIUS = 10

    # Screen dimensions
    SCREEN_X = 600
    SCREEN_Y = 600