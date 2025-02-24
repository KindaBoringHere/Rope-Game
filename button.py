import pygame
from colors import *

pygame.font.init()

pygame.mixer.init()

FONT = pygame.font.Font(None, 44)
button_click_sound = pygame.mixer.Sound(r'co-op game\button.mp3')

class Button:
    def __init__(self, wn, x, y, width, height, color, hover_color, text_color, text_hover_color, text):
        self.wn = wn
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.wn, self.hover_color, self.rect)
            pygame.draw.rect(self.wn, BLACK, self.rect, 3)
        else:
            pygame.draw.rect(self.wn, self.color, self.rect)
            pygame.draw.rect(self.wn, BLACK, self.rect, 3)
        
        text = FONT.render(str(self.text), True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        self.wn.blit(text, text_rect)
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                button_click_sound.play()
                return True
        return False