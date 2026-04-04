"""
Group A: Breakout Game
Contributors: Sida Feng, Baba Diawara, Bianca Fouch, Lucas Tobalsky, Luis Orellana

Description:
This will serve as the main Breakout game launcher.  

"""

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
    
    #constructor to initialize game
    def __init__(self):
        pygame.init()

        #set game window settings
        pygame.display.set_caption("Breakout-Game")
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()

        #game objects (add more add they are added)
        self.ball = Ball(x // 2, y // 2)
        self.paddle = Paddle( x, y)
        self.paddle.using_mouse = True  #need this from biancas paddle.py, if not working make false to use keyboard or comment out
        self.brick_grid = BrickGrid(x)
        self.scoremanager = ScoreManager()
        self.livesmanager = LivesManager()
        self.renderer = Renderer(self.screen)

        self.running = True


    #run game function
    def run_game(self):

        #game loop
        while self.running:
            #frames
            self.clock.tick(Settings.FRAMES.value)

            #Quit (from pygame docs)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #paddle updates
            self.paddle.update()
            ball_check = self.ball.move()

            #check for ball going under the paddle / game over condition
            if ball_check == -1:
                self.livesmanager.lose_life()
                self.ball = Ball(x // 2, y // 2)
                #end loop if lives are out
                if self.livesmanager.current_lives() <= 0:
                    self.running = False

            #check for collisions with paddle
            if self.ball.has_hit(self.paddle) and self.ball.speed_y > 0:
                self.ball.bounce(Settings.VERTICAL)
                self.ball.rect.bottom = self.paddle.rect.top
                
            #Check for collision with bricks
            for brick in self.brick_grid.bricks_array:
                if brick.active and self.ball.has_hit(brick):
                    brick.destroy()
                    self.scoremanager.add(10) # Moved here to update score only when bricks are destroyed
                    self.ball.bounce(Settings.VERTICAL)

                
                #temporary for testing purposes **********************************************
               # self.scoremanager.add(10)

            #render all game objects
            self.renderer.draw(self.ball, self.paddle, self.brick_grid, self.livesmanager, self.scoremanager)

if __name__ == "__main__":
    game = Game()
    game.run_game()
