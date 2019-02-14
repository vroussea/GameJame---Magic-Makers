import contextlib

from game.classes.entity import Entity

with contextlib.redirect_stdout(None):
    import pygame
from pygame import *


class Platform(Entity):
    def __init__(self, screen, pos):
        super().__init__()
        self.rect = pygame.draw.rect(screen, (0, 255, 0), pos)

    def scrolling(self):
        self.rect.move_ip(-1, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
