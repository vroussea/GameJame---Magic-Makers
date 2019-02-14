import contextlib

from os import environ

from game.levels import Levels

with contextlib.redirect_stdout(None):
    import pygame
from pygame import *

from game.entities.character import Character

environ['SDL_VIDEO_CENTERED'] = '1'


def main():
    pygame.init()

    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((width, height))

    h = pygame.display.get_surface().get_height()
    step = h / 10

    timer = pygame.time.Clock()


    time_elapsed_since_last_action = 0

    levels = Levels(screen, step)

    platforms = levels.load_level(1)
    if platforms is None:
        exit(-1)

    player = Character(screen, platforms)

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
            for platform in platforms:
                platform.scrolling()
            time_elapsed_since_last_action = 0

        player.draw(screen)
        for platform in platforms:
            platform.draw(screen)

        pygame.display.update()
        time_elapsed_since_last_action += timer.tick(60)


if __name__ == "__main__":
    main()
