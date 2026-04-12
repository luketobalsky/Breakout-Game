# ----- Unit Test Brick Class -----
from game.brickgrid import BrickGrid
from game.brick import Brick


def test_initialization():
    screen_width = 400
    brick_grid = BrickGrid(screen_width)

    # Expected rows and columns
    expected_columns = int(screen_width / (BrickGrid.PADDING + Brick.WIDTH))
    expected_total_bricks = int(expected_columns * BrickGrid.ROWS)
    assert len(brick_grid.bricks_array) == expected_total_bricks


def test_all_bricks_destroyed_false():
    brick_grid = BrickGrid(400)
    assert brick_grid.all_bricks_destroyed() is False


def test_all_bricks_destroyed_true():
    brick_grid = BrickGrid(400)

    # Destroy bricks
    for brick in brick_grid.bricks_array:
        brick.destroy()
    assert brick_grid.all_bricks_destroyed() is True
