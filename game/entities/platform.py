import contextlib

from game.entities.entity import Entity

with contextlib.redirect_stdout(None):
    import pygame
from pygame import *

class Platform(Entity):
    def __init__(self, screen, pos, step):
        super().__init__()
        self.rect = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pos + (step, step)))

    def scrolling(self):
        self.rect.move_ip(-2, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
