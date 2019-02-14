import contextlib

from game.classes.entity import Entity

with contextlib.redirect_stdout(None):
    import pygame
from pygame import *


class Character(Entity):
    def __init__(self, screen):
        super().__init__()
        x, y = pygame.display.get_surface().get_size()
        self.rect = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((x / 2) - 20, (y / 2) - 20, 40, 40))

    def update(self):
        pressed = pygame.key.get_pressed()
        up = pressed[K_UP]
        down = pressed[K_DOWN]
        left = pressed[K_LEFT]
        right = pressed[K_RIGHT]

        if up:
            self.rect.move_ip(0, -1)
        if down:
            self.rect.move_ip(0, 1)
        if left:
            self.rect.move_ip(-1, 0)
        if right:
            self.rect.move_ip(1, 0)

    def scrolling(self):
        self.rect.move_ip(-1, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
