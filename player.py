import pygame
from colors import *

class Player:
    def __init__(self, color, speed, scale, id, x, y, wn):
        self.color = color
        self.speed = speed
        self.scale = scale
        self.id = id
        self.x = x
        self.y = y
        self.wn = wn
    
    def draw(self):
        pygame.draw.circle(self.wn, self.color, (self.x, self.y), self.scale)
        pygame.draw.circle(self.wn, BLACK, (self.x, self.y), self.scale, 2)
    
    def get_circle(self):
        return pygame.circle(self.x, self.y, self.scale)