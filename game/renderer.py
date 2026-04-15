"""
Group A: Breakout Game
Contributor: Lucas Tobalsky

Description:
The following class initializes the renderer component.
This will set up the GUI for the game

"""
import pygame
from game.settings import Settings


class Renderer:

    # constructor to initialize playing window
    def __init__(self, screen):
        self.screen = screen

    # render components (via componenents draw() )
    # make sure to add components here as needed
    def draw(self, ball, paddle, brick_grid, livesmanager, scoremanager, levelmanager):

        # text renderer/drawer for pygame
        self.font = pygame.font.SysFont(None, 25)

        # makes window specificed color
        self.screen.fill("black")

        # draw componenets to screen (again add componenets here as they are added done by yall)
        ball.draw(self.screen, (255, 255, 255))
        paddle.draw(self.screen)
        brick_grid.draw(self.screen)

        # fetch and display current lives and scores
        lives = self.font.render(
            "Lives: " + str(livesmanager.current_lives()), True, "white")
        score = self.font.render(
            "Score: " + str(scoremanager.current_score()), True, "white")

        level = self.font.render(
            "Level: " + str(levelmanager.get_level()), True, "White")

        # place componenets
        y_placement = Settings.SCREEN_Y.value - 30

        self.screen.blit(lives, (20, y_placement))
        self.screen.blit(level, ((Settings.SCREEN_X.value /
                         2)-40, y_placement))
        self.screen.blit(score, (Settings.SCREEN_X.value -
                         100, y_placement))

        # update screen
        pygame.display.flip()
