"""
Group A: Breakout Game
Contributors: Sida Feng, Baba Diawara, Bianca Fouch, Lucas Tobalsky, Luis Orellana

Description:
This will serve as the Main game loop and state manager for the Breakout game.

This module initializes pygame, loads assets, creates all core game
objects (Ball, Paddle, BrickGrid, ScoreManager, LivesManager, etc.),
and manages the overall game flow including menus, levels, updates,
rendering, and state transitions.
"""

import os
import pygame
from game.paddle import Paddle
from game.ball import Ball
from game.brickgrid import BrickGrid
from game.scoremanager import ScoreManager
from game.livesmanager import LivesManager
from game.renderer import Renderer
from game.settings import Settings
from game.levelmanager import LevelManager
from game.difficultymanager import DifficultyManager

# import settings
X = Settings.SCREEN_WIDTH.value
Y = Settings.SCREEN_HEIGHT.value


class Game:
    """
    Central controller for the Breakout game.

    The Game class initializes pygame, loads sounds, creates all game
    objects, and manages the main loop. It handles input events, game
    states (menu, running, next level, win, game over), collision
    processing, scoring, lives, and rendering.

    Responsibilities:
    - Initialize and configure the game window and audio.
    - Manage game states and transitions.
    - Update all game objects each frame.
    - Detect collisions and apply game logic.
    - Render menus, gameplay, and end screens.
    """

    def __init__(self):
        """Initializes pygame, loads assets, creates game objects, and sets initial game state."""
        pygame.init()
        pygame.mixer.init()

        # collision sound
        self.collision_sound = pygame.mixer.Sound(
            os.path.join("game", "sounds", "CollisionSound.wav"))
        self.collision_sound.set_volume(0.2)

        # ball drop sound
        self.ball_drops_sound = pygame.mixer.Sound(
            os.path.join("game", "sounds", "BallDrop.wav"))
        self.ball_drops_sound.set_volume(0.2)

        # win sound
        self.win_sound = pygame.mixer.Sound(os.path.join("game", "sounds", "win.wav"))

        # lose sound
        self.lose_sound = pygame.mixer.Sound(os.path.join("game", "sounds", "lose.wav"))

        # difficulty manager
        self.difficulty_manager = DifficultyManager()

        # window setup
        pygame.display.set_caption("Breakout-Game")
        self.screen = pygame.display.set_mode((X, Y))
        self.clock = pygame.time.Clock()

        # game objects
        self.ball = Ball()
        self.paddle = Paddle()
        self.brick_grid = BrickGrid()
        self.paddle.using_mouse = True
        self.score_manager = ScoreManager()
        self.lives_manager = LivesManager()
        self.level_manager = LevelManager()
        self.renderer = Renderer(self.screen)

        # game state
        self.state = "main_menu"

        # UI buttons
        self.restart_button = pygame.Rect(X // 2 - 50, Y // 2 - 25, 100, 50)
        self.continue_button = pygame.Rect(X // 2 - 50, Y // 2 - 25, 100, 50)
        self.start_button = pygame.Rect(X // 2 - 50, Y // 2 - 25, 100, 50)
        self.quit_button = pygame.Rect(X // 2 - 50, Y // 2 + 50, 100, 50)
        self.menu_button = pygame.Rect(X // 2 - 50, Y // 2 + 50, 100, 50)

    def run_game(self):
        """
        Main game loop. Handles frame timing, input events, state transitions,
        and delegates drawing or updating based on the current game state.
        """
        while True:
            self.clock.tick(Settings.FRAMES.value)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "main_menu":
                        if self.start_button.collidepoint(event.pos):
                            self.reset_game()
                            self.state = "running"
                        elif self.quit_button.collidepoint(event.pos):
                            pygame.quit()

                if self.state == "game_over":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.restart_button.collidepoint(event.pos):
                            self.reset_game()
                            self.state = "running"
                        elif self.menu_button.collidepoint(event.pos):
                            self.state = "main_menu"

                if self.state == "next_level":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.continue_button.collidepoint(event.pos):
                            self.setup_level()
                            self.state = "running"
                        elif self.menu_button.collidepoint(event.pos):
                            self.state = "main_menu"

                if self.state == "win":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.restart_button.collidepoint(event.pos):
                            self.reset_game()
                            self.state = "running"
                        elif self.menu_button.collidepoint(event.pos):
                            self.state = "main_menu"

            if self.state == "main_menu":
                self.draw_main_menu()
            if self.state == "running":
                self.update_game()
            if self.state == "next_level":
                self.draw_next_level_screen()
            if self.state == "win":
                self.draw_win_screen()
            elif self.state == "game_over":
                self.draw_restart_screen()

    def update_game(self):
        """
        Updates all active game objects during gameplay.

        Handles paddle movement, ball movement, collision detection with
        paddle and bricks, scoring, life loss, level progression, and
        triggers state changes such as win or game over.
        """
        self.paddle.move()
        ball_check = self.ball.move()

        # ball fell below screen
        if ball_check == -1:
            self.lives_manager.lose_life()
            self.ball_drops_sound.play()
            self.ball = Ball()
            self.difficulty_manager.increase_difficulty(self.ball, self.level_manager.get_level())

            if self.lives_manager.current_lives() <= 0:
                self.state = "game_over"
                self.lose_sound.play()

        # paddle collision
        if self.ball.has_hit(self.paddle) and self.ball.speed_y > 0:
            self.ball.bounce(Settings.VERTICAL)
            self.collision_sound.play()
            self.ball.rect.bottom = self.paddle.rect.top

        # brick collisions
        for brick in self.brick_grid.bricks_array:
            if brick.active and self.ball.has_hit(brick):
                brick.destroy()
                self.score_manager.add(10)
                self.ball.bounce(Settings.VERTICAL)
                self.collision_sound.play()

        # level cleared
        if self.brick_grid.all_bricks_destroyed():
            self.level_manager.increment_level()
            if self.difficulty_manager.final_level(self.level_manager.get_level()):
                self.state = "win"
                self.win_sound.play()
            else:
                self.state = "next_level"

        # render
        self.renderer.draw(self.ball, self.paddle, self.brick_grid,
                           self.lives_manager, self.score_manager, self.level_manager)

    def draw_main_menu(self):
        """Renders the main menu screen with Start and Quit buttons."""
        self.screen.fill((0, 0, 0))

        pygame.draw.rect(self.screen, (0, 128, 255), self.start_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.quit_button)

        font = pygame.font.Font(None, 30)
        text = font.render("Start", True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=self.start_button.center))

        text2 = font.render("Quit", True, (255, 255, 255))
        self.screen.blit(text2, text2.get_rect(center=self.quit_button.center))

        title_font = pygame.font.Font(None, 60)
        title_text = title_font.render("Breakout", True, (255, 255, 255))
        self.screen.blit(title_text, title_text.get_rect(center=(X // 2, Y // 2 - 80)))

        pygame.display.flip()

    def draw_restart_screen(self):
        """Renders the Game Over screen with Restart and Menu options."""
        self.screen.fill((0, 0, 0))

        pygame.draw.rect(self.screen, (0, 128, 255), self.restart_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.menu_button)

        font = pygame.font.Font(None, 30)
        text = font.render("Restart", True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=self.restart_button.center))

        text2 = font.render("Menu", True, (255, 255, 255))
        self.screen.blit(text2, text2.get_rect(center=self.menu_button.center))

        game_over_font = pygame.font.Font(None, 60)
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(game_over_text, game_over_text.get_rect(center=(X // 2, Y // 2 - 80)))

        pygame.display.flip()

    def draw_next_level_screen(self):
        """Renders the Next Level screen and Continue button."""
        self.screen.fill((0, 0, 0))

        pygame.draw.rect(self.screen, (0, 128, 255), self.continue_button)

        font = pygame.font.Font(None, 30)
        text = font.render("Continue", True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=self.continue_button.center))

        continue_font = pygame.font.Font(None, 60)
        continue_text = continue_font.render("Next Level", True, (255, 255, 255))
        self.screen.blit(continue_text, continue_text.get_rect(center=(X // 2, Y // 2 - 80)))

        pygame.display.flip()

    def draw_win_screen(self):
        """Renders the Win screen with Play Again and Menu options."""
        self.screen.fill((0, 0, 0))

        pygame.draw.rect(self.screen, (0, 128, 255), self.restart_button)
        pygame.draw.rect(self.screen, (0, 128, 255), self.menu_button)

        font = pygame.font.Font(None, 30)
        text = font.render("Play again", True, (255, 255, 255))
        self.screen.blit(text, text.get_rect(center=self.restart_button.center))

        text2 = font.render("Menu", True, (255, 255, 255))
        self.screen.blit(text2, text2.get_rect(center=self.menu_button.center))

        win_font = pygame.font.Font(None, 60)
        win_text = win_font.render("You Won!", True, (255, 255, 255))
        self.screen.blit(win_text, win_text.get_rect(center=(X // 2, Y // 2 - 80)))

        pygame.display.flip()

    def reset_game(self):
        """Resets score, lives, level, and prepares the game for a new run."""
        self.score_manager = ScoreManager()
        self.lives_manager = LivesManager()
        self.level_manager = LevelManager()
        self.setup_level()

    def setup_level(self):
        """
        Initializes a new level by creating a fresh ball, paddle, and brick grid,
        and applying difficulty scaling based on the current level.
        """
        self.ball = Ball()
        self.paddle = Paddle()
        self.paddle.using_mouse = True
        self.brick_grid = BrickGrid()

        self.difficulty_manager.increase_difficulty(self.ball, self.level_manager.get_level())


if __name__ == "__main__":
    game = Game()
    game.run_game()
