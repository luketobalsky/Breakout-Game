"""
Group A: Breakout Game
Contributor: Lucas Tobalsky

Description:
This module defines the Renderer class, which is responsible for drawing all
game components to the screen, including the ball, paddle, brick grid,
and UI elements such as lives, score, and level.
"""

import pygame
from game.settings import Settings


class Renderer:
    """
    Handles all rendering operations for the Breakout game.

    Draws game objects, UI text, and manages screen updates. The Renderer
    centralizes all drawing logic so other classes remain focused on game
    behavior rather than display concerns.
    """

    def __init__(self, screen):
        """
        Initializes the renderer with the given screen surface.

        Parameters:
            screen (pygame.Surface): The main game window surface.
        """
        self.screen = screen

    def draw(self, ball, paddle, brick_grid, lives_manager, score_manager, level_manager):
        """
        Draws all game components and UI elements to the screen.

        Parameters:
            ball (Ball): The ball object to render.
            paddle (Paddle): The player's paddle.
            brick_grid (BrickGrid): The grid of bricks.
            lives_manager (LivesManager): Tracks remaining player lives.
            score_manager (ScoreManager): Tracks the player's score.
            level_manager (LevelManager): Tracks the current level.
        """
        # Text renderer
        self.font = pygame.font.SysFont(None, 25)

        # Clear screen
        self.screen.fill("black")

        # Draw game components
        ball.draw(self.screen)
        paddle.draw(self.screen)
        brick_grid.draw(self.screen)

        # UI text
        lives = self.font.render(
            "Lives: " + str(lives_manager.current_lives()), True, "white"
        )
        score = self.font.render(
            "Score: " + str(score_manager.current_score()), True, "white"
        )
        level = self.font.render(
            "Level: " + str(level_manager.get_level()), True, "white"
        )

        # UI placement
        y_placement = Settings.SCREEN_HEIGHT.value - 30

        self.screen.blit(lives, (20, y_placement))
        self.screen.blit(level, ((Settings.SCREEN_WIDTH.value / 2) - 40, y_placement))
        self.screen.blit(score, (Settings.SCREEN_WIDTH.value - 100, y_placement))

        # Update display
        pygame.display.flip()
