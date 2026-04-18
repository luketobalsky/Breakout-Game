# ----- Unit Test Brick Class -----
from game.brickgrid import BrickGrid
from game.settings import Settings


def test_initialization():
    brick_grid = BrickGrid()

    # Expected rows and columns
    expected_columns = int(Settings.SCREEN_WIDTH.value /
                           (Settings.GRID_PADDING.value + Settings.BRICK_WIDTH.value))
    expected_total_bricks = int(expected_columns * Settings.GRID_ROWS.value)
    assert len(brick_grid.bricks_array) == expected_total_bricks


def test_all_bricks_destroyed_false():
    brick_grid = BrickGrid()
    assert brick_grid.all_bricks_destroyed() is False


def test_all_bricks_destroyed_true():
    brick_grid = BrickGrid()

    # Destroy bricks
    for brick in brick_grid.bricks_array:
        brick.destroy()
    assert brick_grid.all_bricks_destroyed() is True
