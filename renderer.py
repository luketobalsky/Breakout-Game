# This will be the renderer class which will set up the GUI for the game

# Contributor: Lucas Tobalsky

import pygame

class Renderer:
    
    #constructor to initialize playing window
    def __init__(self, screen):
        self.screen = screen

    #render components (via componenents draw() )
    def draw(self, ball, paddle, livesmanager, scoremanager):         #make sure to add components here as needed

        #text renderer/drawer for pygame
        self.font = pygame.font.SysFont(None, 25)

        #makes window specificed color
        self.screen.fill("black")

        #draw componenets to screen (again add componenets here as they are added done by yall)
        ball.draw(self.screen, (255, 255, 255))
        paddle.draw(self.screen)

        #fetch and display current lives and scores
        lives = self.font.render("Lives: " + str(livesmanager.current_lives()), True, "white")
        score = self.font.render("Score: " + str(scoremanager.current_score()), True, "white")

        #place componenets 
        self.screen.blit(lives, (10, 10))
        self.screen.blit(score, (900, 10))

        #update screen
        pygame.display.flip()
