import contextlib

from os import environ

with contextlib.redirect_stdout(None):
    import pygame
from pygame import *

from game.classes.character import Character

environ['SDL_VIDEO_CENTERED'] = '1'

def main():
    pygame.init()
    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((width, height))
    timer = pygame.time.Clock()

    player = Character(screen)
    time_elapsed_since_last_action = 0

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return

        player.update()

        screen.fill((0, 0, 0))

        if time_elapsed_since_last_action > 1:
            player.scrolling()
            time_elapsed_since_last_action = 0

        player.draw(screen)

        pygame.display.update()
        time_elapsed_since_last_action += timer.tick()
        timer.tick(60)


if __name__ == "__main__":
    main()
