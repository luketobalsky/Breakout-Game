# ----- Unit Test Paddle Class-----
from game.paddle import Paddle


def test_initialization():
    screen_width = 400
    screen_height = 400
    paddle = Paddle(screen_width, screen_height)

    expected_x = screen_width // 2 - paddle.width // 2
    expected_y = screen_height - paddle.height - 50

    assert paddle.rect.x == expected_x
    assert paddle.rect.y == expected_y
    assert paddle.width == 100
    assert paddle.height == 15
    assert paddle.speed == 10
