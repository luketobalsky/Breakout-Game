# This will be the score manager class which will track the players score

# Contributor: Lucas Tobalsky

#import pygame

class ScoreManager:

    #create and set initial score to 0
    def __init__(self):
        self.score = 0

    #add points to score
    def add(self, points):
        self.score += points

    #get your current score
    def current_score(self):
        return self.score
    
    #clear/reset score to 0
    def clear(self):
        self.score = 0