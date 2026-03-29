import pygame
from pygame import *
from paddle import Paddle
from brick import Brick
from settings import Settings


"""
The ball class represent the blueprint necessary to create a ball object.
"""
class Ball:
    collision_threshold = 5

    def __init__(self, x, y):
        self.radius = 10
        self.width = self.radius * 2
        self.height = self.radius * 2
        self.x = x - self.radius
        self.y = y
        self.frame = Rect(self.x, self.y, self.width, self.height)
        self.speed_x = 4
        self.speed_y = -4

    def move(self):
        # Screen Collision Handling
        if self.frame.left < 0 or self.frame.right > Settings.SCREEN_X:
            self.bounce(Settings.HORIZONTAL)
        if self.frame.top < 0:
            self.bounce(Settings.VERTICAL)
        if self.frame.bottom > Settings.SCREEN_Y:
            self.game_over = -1

        # Ball Movement
        self.frame.x += self.speed_x
        self.frame.y += self.speed_y

    def bounce(self, direction: Settings):
        match direction:
            case Settings.VERTICAL:
                self.speed_y *= -1
            case Settings.HORIZONTAL:
                self.speed_x *= -1

    def hit(self, item):
        if isinstance(item, Paddle):
            if self.frame.colliderect(item.frame):
                if abs(self.frame.bottom - item.frame.top) < self.collision_threshold \
                        and self.speed_y > 0:
                    return True
        elif isinstance(item, Brick):
            if self.frame.colliderect(item.frame):
                # bounce verti
                if abs(self.frame.bottom - item.frame.top < self.collision_threshold
                       and self.speed_y > 0):
                    return True
                if abs(self.frame.top - item.frame.bottom < self.collision_threshold
                       and self.speed_y < 0):
                    return True
                # bounce hori
                if abs(self.frame.right - item.frame.left < self.collision_threshold
                       and self.speed_x > 0):
                    return True
                if abs(self.frame.left - item.frame.right < self.collision_threshold
                       and self.speed_x < 0):
                    return True

    def draw(self, screen, colour):
        pygame.draw.circle(screen, colour,
                           (self.frame.x + self.radius, self.frame.y + self.radius), self.radius)
