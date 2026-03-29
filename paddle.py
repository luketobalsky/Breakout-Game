#This will be the paddle class with the associated mechanics

import pygame
from components import Components

class Paddle:
    def __init__(self, screen_width, screen_height):
        self.width = 100
        self.height = 15
        self.speed = 10

        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height - self.height - 50

        self.screen_width = screen_width

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        #Input states
        self.left_pressed = False
        self.right_pressed = False

        #Mouse tracking
        self.using_mouse = False

    def update(self):
        #mouse movement
        if self.using_mouse:
            mouse_x = pygame.mouse.get_pos()[0]
            self.rect.x = mouse_x - self.width // 2
        else:
            #Keyboard movement
            if self.left_pressed:
                self.rect.x -= self.speed
            if self.right_pressed:
                self.rect.x += self.speed

        # Keep the paddle within the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + self.width > self.screen_width:
            self.rect.x = self.screen_width - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)




