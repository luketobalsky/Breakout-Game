# ----- Unit Test Ball Class-----
from game.ball import Ball
from game.settings import Settings


def test_initialization():

    ball = Ball()

    assert ball.x == Settings.BALL_X.value
    assert ball.y == Settings.BALL_Y.value
    assert ball.width == Settings.BALL_WIDTH.value
    assert ball.height == Settings.BALL_HEIGHT.value
    assert ball.speed_x == Settings.BALL_SPEED_X.value
    assert ball.speed_y == Settings.BALL_SPEED_Y.value
    assert ball.collision_side is None


def test_move():

    ball = Ball()
    expected_x = ball.x + ball.speed_x
    expected_y = ball.y + ball.speed_y

    ball.move()

    assert ball.rect.x == expected_x
    assert ball.rect.y == expected_y


def test_bounce():

    ball = Ball()
    expected_speed_y = ball.speed_y * -1
    expected_speed_x = ball.speed_x * -1

    ball.bounce(Settings.VERTICAL)
    ball.bounce(Settings.HORIZONTAL)

    assert ball.speed_y == expected_speed_y
    assert ball.speed_x == expected_speed_x

