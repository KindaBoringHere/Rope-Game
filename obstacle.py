import pygame
from colors import *

class Obstacle:
    def __init__(self, wn, width, height, x, y, speed, color, hit):
        self.wn = wn
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.hit = hit
    
    def draw(self):
        pygame.draw.rect(self.wn, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.wn, BLACK, (self.x, self.y, self.width, self.height), 2)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def move(self):
        self.y += self.speed