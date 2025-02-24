import pygame
from colors import *

class Line:
    def __init__(self, color, width: int, wn: pygame.Surface, player_1: object, player_2: object):
        self.color = color
        self.width = width
        self.wn = wn
        self.player_1 = player_1
        self.player_2 = player_2
        self.mask = None

    def update_mask(self):
        # Create a surface for the line
        line_surface = pygame.Surface((self.wn.get_width(), self.wn.get_height()), pygame.SRCALPHA)
        line_surface.fill((0, 0, 0, 0))  # Fill with transparent color

        # Draw the line on the surface
        pygame.draw.line(line_surface, self.color, (self.player_1.x, self.player_1.y), (self.player_2.x, self.player_2.y), self.width)

        # Create a mask from the surface
        self.mask = pygame.mask.from_surface(line_surface)

    def draw(self):
        pygame.draw.line(self.wn, (self.color), (self.player_1.x, self.player_1.y), (self.player_2.x, self.player_2.y), self.width)
        self.update_mask()

    def collides_with(self, other_rect):
        if self.mask is None:
            self.update_mask()

        # Get the offset between the line and the other rect
        offset = (other_rect.left, other_rect.top)

        # Check for collision
        return self.mask.overlap(pygame.mask.Mask((other_rect.width, other_rect.height), fill=True), offset) is not None