import contextlib

from game.entities.entity import Entity

with contextlib.redirect_stdout(None):
    import pygame
from pygame import *


class Character(Entity):
    def __init__(self, screen, platforms):
        super().__init__()
        x, y = pygame.display.get_surface().get_size()
        self.rect = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((x / 2) - 20, (y / 2) - 20, 40, 40))
        self.Y_vel = 0
        self.X_vel = 0
        self.platforms = platforms
        self.onGround = False

    def update(self):
        pressed = pygame.key.get_pressed()
        up = pressed[K_UP]
        left = pressed[K_LEFT]
        right = pressed[K_RIGHT]

        self.X_vel = 0
        if up:  # and self.onGround is True:
            self.Y_vel = -8
        else:
            self.Y_vel += 0.2 if self.Y_vel < 8 else 0
        if left:
            self.X_vel = -5
        if right:
            self.X_vel = 5
        self.rect.left += self.X_vel
        self.collide(self.X_vel, 0, self.platforms)
        self.rect.top += self.Y_vel
        self.onGround = False
        self.collide(0, self.Y_vel, self.platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.Y_vel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def scrolling(self):
        self.rect.move_ip(-2, 0)
        # for platform in self.platforms:
        #   platform.draw(self.screen)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

    def set_platforms(self, platforms):
        self.platforms = platforms
