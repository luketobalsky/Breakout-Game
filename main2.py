
import pygame
from paddle import Paddle
from ball import Ball
#from brick import Brick
from brickgrid import BrickGrid
from scoremanager import ScoreManager
from livesmanager import LivesManager
#from collisionmanager import CollisionManager
#from difficultymanager import DifficultyManager
from renderer import Renderer
from settings import Settings

#import settings
x = Settings.SCREEN_X.value
y = Settings.SCREEN_Y.value


class Game:
    # constructor to initialize game
    def __init__(self):
        pygame.init()

        # set game window settings
        pygame.display.set_caption("Breakout-Game")
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()

        # game objects (add more add they are added)
        self.ball = Ball(x // 2, y // 2)
        self.paddle = Paddle(x, y)
        self.brick_grid = BrickGrid(x)
        # need this from biancas paddle.py, if not working make false to use keyboard or comment out
        self.paddle.using_mouse = True
        self.scoremanager = ScoreManager()
        self.livesmanager = LivesManager()
        self.renderer = Renderer(self.screen)

        # game state
        self.state = "running"
        self.restart_button = pygame.Rect(x // 2 - 50, y // 2 - 25, 100, 50)

    # run game function

    def run_game(self):
        # game loop
        while True:
            # frames
            self.clock.tick(Settings.FRAMES.value)

            # Quit (from pygame docs)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if self.state == "game_over":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.restart_button.collidepoint(event.pos):
                            self.reset_game()

            if self.state == "running":
                self.update_game()
            elif self.state == "game_over":
                self.draw_restart_screen()

    def update_game(self):

        # paddle updates
        self.paddle.update()
        ball_check = self.ball.move()

        # check for ball going under the paddle / game over condition
        if ball_check == -1:
            self.livesmanager.lose_life()
            self.ball = Ball(x // 2, y // 2)
            # end loop if lives are out
            if self.livesmanager.current_lives() <= 0:
                self.state = "game_over"

        # check for collisions with paddle
        if self.ball.has_hit(self.paddle) and self.ball.speed_y > 0:
            self.ball.bounce(Settings.VERTICAL)
            self.ball.rect.bottom = self.paddle.rect.top

        # check collison with bricks
        for brick in self.brick_grid.bricks_array:
            if brick.active and self.ball.has_hit(brick):
                brick.destroy()
                self.scoremanager.add(10)
                self.ball.bounce(Settings.VERTICAL)

        # render all game objects
        self.renderer.draw(self.ball, self.paddle, self.brick_grid,
                           self.livesmanager, self.scoremanager)

    def draw_restart_screen(self):
        self.screen.fill((0, 0, 0))

        # draw button

        pygame.draw.rect(self.screen, (0, 128, 255), self.restart_button)

        # button text
        font = pygame.font.Font(None, 36)
        text = font.render("Restart", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.restart_button.center)
        self.screen.blit(text, text_rect)

        # "Game Over" text
        game_over_font = pygame.font.Font(None, 60)
        game_over_text = game_over_font.render(
            "Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(x // 2, y // 2 - 80))
        self.screen.blit(game_over_text, game_over_rect)

        pygame.display.flip()

    def reset_game(self):
        # reset all game objects
        self.ball = Ball(x // 2, y // 2)
        self.paddle = Paddle(x, y)
        self.paddle.using_mouse = True
        self.brick_grid = BrickGrid(x)

        self.scoremanager = ScoreManager()
        self.livesmanager = LivesManager()

        self.state = "running"


if __name__ == "__main__":
    game = Game()
    game.run_game()
