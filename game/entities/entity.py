import contextlib

with contextlib.redirect_stdout(None):
    import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
