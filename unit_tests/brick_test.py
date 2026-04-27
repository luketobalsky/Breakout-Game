# ----- Unit Test Brick Class -----
from game.brick import Brick
from game.settings import Settings


def test_initialization():
    brick = Brick(10, 20, "red")

    assert brick.x == 10
    assert brick.y == 20
    assert brick.color == (255, 0, 0)
    assert brick.active is True

    assert brick.rect.x == 10
    assert brick.rect.y == 20
    assert brick.rect.width == Settings.BRICK_WIDTH.value
    assert brick.rect.height == Settings.BRICK_HEIGHT.value


def test_brick_destroy():
    brick = Brick(10, 10)
    brick.destroy()
    assert brick.active is False
