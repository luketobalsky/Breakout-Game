"""
Group A: Breakout Game
Contributors: Sida Feng, Baba Diawara, Bianca Fouch, Lucas Tobalsky, Luis Orellana

Description:
This will serve as the main Breakout game launcher.

"""


import pygame
from game.paddle import Paddle
from game.ball import Ball
from game.brickgrid import BrickGrid
from game.scoremanager import ScoreManager
from game.livesmanager import LivesManager
from game.renderer import Renderer
from game.settings import Settings
from game.levelmanager import LevelManager

# import settings
x = Settings.SCREEN_X.value
y = Settings.SCREEN_Y.value


class Game:
    # constructor to initialize game
    def __init__(self):
        pygame.init()

        # Load mixer
        pygame.mixer.init()

        # collision sound
        self.collision_sound = pygame.mixer.Sound(
            "game/sounds/CollisionSound.wav")
        self.collision_sound.set_volume(0.2)

        # ball drop sound
        self.ball_drops_sound = pygame.mixer.Sound("game/sounds/BallDrop.wav")
        self.ball_drops_sound.set_volume(0.2)

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
        self.levelmanager = LevelManager()
        self.renderer = Renderer(self.screen)

        # game state
        self.state = "running"

        # game state buttons
        self.restart_button = pygame.Rect(x // 2 - 50, y // 2 - 25, 100, 50)
        self.continue_button = pygame.Rect(x // 2 - 50, y // 2 - 25, 100, 50)

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
                            self.state = "running"
                if self.state == "next_level":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.continue_button.collidepoint(event.pos):
                            self.setup_level()
                            self.state = "running"
                if self.state == "win":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.restart_button.collidepoint(event.pos):
                            self.reset_game()
                            self.state = "running"

            if self.state == "running":
                self.update_game()
            if self.state == "next_level":
                self.draw_next_level_screen()
            if self.state == "win":
                self.draw_win_screen()
            elif self.state == "game_over":
                self.draw_restart_screen()

    def update_game(self):

        # paddle updates
        self.paddle.update()
        ball_check = self.ball.move()

        # check for ball going under the paddle / game over condition
        if ball_check == -1:
            self.livesmanager.lose_life()
            self.ball_drops_sound.play()
            self.ball = Ball(x // 2, y // 2)
            self.apply_ball_level_speed()
            # end loop if lives are out
            if self.livesmanager.current_lives() <= 0:
                self.state = "game_over"

        # check for collisions with paddle
        if self.ball.has_hit(self.paddle) and self.ball.speed_y > 0:
            self.ball.bounce(Settings.VERTICAL)
            self.collision_sound.play()
            self.ball.rect.bottom = self.paddle.rect.top

        # check collison with bricks
        for brick in self.brick_grid.bricks_array:
            if brick.active and self.ball.has_hit(brick):
                brick.destroy()
                self.scoremanager.add(10)
                self.ball.bounce(Settings.VERTICAL)
                self.collision_sound.play()

        if self.brick_grid.all_bricks_destroyed():
            self.levelmanager.increment_level()
            if self.levelmanager.get_level() > 3:
                self.state = "win"
            else:
                self.state = "next_level"

        # render all game objects
        self.renderer.draw(self.ball, self.paddle, self.brick_grid,
                           self.livesmanager, self.scoremanager)

    def draw_restart_screen(self):
        self.screen.fill((0, 0, 0))

        # draw button
        pygame.draw.rect(self.screen, (0, 128, 255), self.restart_button)

        # button text
        font = pygame.font.Font(None, 30)
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

    def draw_next_level_screen(self):
        self.screen.fill((0, 0, 0))

        # draw button
        pygame.draw.rect(self.screen, (0, 128, 255), self.continue_button)

        # button text
        font = pygame.font.Font(None, 30)
        text = font.render("Continue", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.continue_button.center)
        self.screen.blit(text, text_rect)

        # "Continue" text
        continue_font = pygame.font.Font(None, 60)
        continue_text = continue_font.render(
            "Continue to next level?", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(x // 2, y // 2 - 80))
        self.screen.blit(continue_text, continue_rect)

        pygame.display.flip()

    def draw_win_screen(self):
        self.screen.fill((0, 0, 0))

        # draw button
        pygame.draw.rect(self.screen, (0, 128, 255), self.restart_button)

        # button text
        font = pygame.font.Font(None, 30)
        text = font.render("Play again", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.restart_button.center)
        self.screen.blit(text, text_rect)

        # "You won" text
        game_over_font = pygame.font.Font(None, 60)
        game_over_text = game_over_font.render(
            "You Won!", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(x // 2, y // 2 - 80))
        self.screen.blit(game_over_text, game_over_rect)

        pygame.display.flip()

    def reset_game(self):
        # reset game objects
        self.scoremanager = ScoreManager()
        self.livesmanager = LivesManager()
        self.levelmanager = LevelManager()
        self.setup_level()

    # Level transitions
    def setup_level(self):
        self.ball = Ball(x // 2, y // 2)
        self.paddle = Paddle(x, y)
        self.paddle.using_mouse = True
        self.brick_grid = BrickGrid(x)

        level = self.levelmanager.get_level()

        if level == 2:
            self.ball.speed_x = 6
            self.ball.speed_y = -6
        elif level == 3:
            self.ball.speed_x = 8
            self.ball.speed_y = -8

    def apply_ball_level_speed(self):
        level = self.levelmanager.get_level()
        if level == 2:
            self.ball.speed_x = 6
            self.ball.speed_y = -6
        elif level == 3:
            self.ball.speed_x = 8
            self.ball.speed_y = -8


if __name__ == "__main__":
    game = Game()
    game.run_game()
