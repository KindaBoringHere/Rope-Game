import pygame
from colors import *

pygame.font.init()

TITLE_FONT = pygame.font.Font(None,35)
DESC_FONT = pygame.font.Font(None, 25)

class First_time():
    def __init__(self,wn,y):
        self.y = y
        self.name = "That Was Only The Tutorial?"
        self.description = "Finish your first run"
        self.unlocked: bool = False
        self.wn = wn

    def draw(self):
        

        if self.unlocked:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,GREEN,(170,self.y,500,100))
        else:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,RED,(170,self.y,500,100))

        pygame.draw.rect(self.wn,BLACK,(170,self.y,500,100),5)
        
        self.wn.blit(title_text,(180,self.y+10))
        self.wn.blit(desc_text,(180,self.y+50))

class fifth_time():
    def __init__(self,wn,y):
        self.y = y
        self.name = "Shooting For The Long Run"
        self.description = "Finish your 50th run"
        self.unlocked: bool = False
        self.wn = wn

    def draw(self):


        if self.unlocked:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,GREEN,(170,self.y,500,100))
        else:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,RED,(170,self.y,500,100))

        pygame.draw.rect(self.wn,BLACK,(170,self.y,500,100),5)
        
        self.wn.blit(title_text,(180,self.y+10))
        self.wn.blit(desc_text,(180,self.y+50))

class ten_coins():
    def __init__(self,wn,y):
        self.y = y
        self.name = "Are We Considered Rich Now?"
        self.description = "Collect 10 coins"
        self.unlocked: bool = False
        self.wn = wn

    def draw(self):

        if self.unlocked:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,GREEN,(170,self.y,500,100))
        else:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,RED,(170,self.y,500,100))
        pygame.draw.rect(self.wn,BLACK,(170,self.y,500,100),5)
        
        self.wn.blit(title_text,(180,self.y+10))
        self.wn.blit(desc_text,(180,self.y+50))

class ten_k_score():
    def __init__(self,wn,y):
        self.y = y
        self.name = "Practice Makes Perfect"
        self.description = "Achieve 50k score in a single run"
        self.unlocked: bool = False
        self.wn = wn

    def draw(self):
        

        if self.unlocked:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,GREEN,(170,self.y,500,100))
        else:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,RED,(170,self.y,500,100))
        pygame.draw.rect(self.wn,BLACK,(170,self.y,500,100),5)
        
        self.wn.blit(title_text,(180,self.y+10))
        self.wn.blit(desc_text,(180,self.y+50))

class tweney_coins_single_run():
    def __init__(self,wn,y):
        self.y = y
        self.name = "Money Time!"
        self.description = "Collect 20 coins in a single run"
        self.unlocked: bool = False
        self.wn = wn

    def draw(self):
        

        if self.unlocked:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,GREEN,(170,self.y,500,100))
        else:
            title_text = TITLE_FONT.render(self.name,True,BLACK)
            desc_text = DESC_FONT.render(self.description,True,BLACK)
            pygame.draw.rect(self.wn,RED,(170,self.y,500,100))
        pygame.draw.rect(self.wn,BLACK,(170,self.y,500,100),5)
        
        self.wn.blit(title_text,(180,self.y+10))
        self.wn.blit(desc_text,(180,self.y+50))


