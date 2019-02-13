#! /usr/bin/python

import contextlib

with contextlib.redirect_stdout(None):
    import pygame
from pygame import *


def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.init()
    timer = pygame.time.Clock()

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return

        screen.fill((0, 0, 0))
        pygame.display.update()
        timer.tick(60)


if __name__ == "__main__":
    main()
