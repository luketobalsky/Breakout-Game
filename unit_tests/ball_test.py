# ----- Unit Test Ball Class-----
from game.ball import Ball
from game.settings import Settings


def test_initialization():
    x = 50
    y = 100

    ball = Ball(x, y)

    assert ball.x == x - Settings.RADIUS.value
    assert ball.y == y
    assert ball.width == Settings.RADIUS.value * 2
    assert ball.height == Settings.RADIUS.value * 2
    assert ball.speed_x == 4
    assert ball.speed_y == -4
    assert ball.collision_side is None
