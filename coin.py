import pygame
from colors import *

class Coin:
    def __init__(self, wn, x, y, scale, color, speed):
        self.wn = wn
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.speed = speed
        self.collected: bool = False

    def draw(self):
        pygame.draw.circle(self.wn, self.color, (self.x, self.y), self.scale)
        pygame.draw.circle(self.wn, BLACK, (self.x, self.y), self.scale, 2)
    
    def move(self):
        self.y += self.speed
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.scale, self.scale)