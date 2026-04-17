# This will be the difficulty manager class which will manage the game difficulty as the player progresses

class DifficultyManager:
    
    def __init__(self):
        self.base_speed = 4
        self.speed_increment = 2
        self.max_level = 3

    def increase_difficulty(self, ball, level):
        speed = self.base_speed + (level - 1) * self.speed_increment
        ball.speed_x = speed
        ball.speed_y = -speed

    def final_level(self, level):
        return level > self.max_level