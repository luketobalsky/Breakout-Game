# This will be the lives manager class which will track the players available/used lives

# Contributor: Lucas Tobalsky

from settings import Settings

class LivesManager:

    #create and set lives to starting value
    def __init__(self):
        self.lives = Settings.LIVES.value

    #check if you have lives left and remove one
    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1

    #get your current lives
    def current_lives(self):
        return self.lives
    
    #clear/reset lives to starting amount
    def clear(self):
        self.lives = Settings.LIVES.value