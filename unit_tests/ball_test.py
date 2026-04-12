# ----- Unit Test Ball Class-----
from game.ball import Ball
from game.settings import Settings
from game.paddle import Paddle
from game.brick import Brick

x = 50
y = 100


def test_initialization():

    ball = Ball(x, y)

    assert ball.x == x - Settings.RADIUS.value
    assert ball.y == y
    assert ball.width == Settings.RADIUS.value * 2
    assert ball.height == Settings.RADIUS.value * 2
    assert ball.speed_x == 4
    assert ball.speed_y == -4
    assert ball.collision_side is None


def test_move():

    ball = Ball(x, y)
    expected_x = (x - Settings.RADIUS.value) + ball.speed_x
    expected_y = y + ball.speed_y

    ball.move()

    assert ball.rect.x == expected_x
    assert ball.rect.y == expected_y


def test_bounce():

    ball = Ball(x, y)
    expected_speed_y = ball.speed_y * -1
    expected_speed_x = ball.speed_x * -1

    ball.bounce(Settings.VERTICAL)
    ball.bounce(Settings.HORIZONTAL)

    assert ball.speed_y == expected_speed_y
    assert ball.speed_x == expected_speed_x
