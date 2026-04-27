# ----- Unit Test Paddle Class-----
from game.paddle import Paddle
from game.settings import Settings


def test_initialization():

    paddle = Paddle()

    assert paddle.width == Settings.PADDLE_WIDTH.value
    assert paddle.height == Settings.PADDLE_HEIGHT.value
    assert paddle.speed == Settings.PADDLE_SPEED.value

