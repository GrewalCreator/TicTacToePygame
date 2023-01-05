from PygameSetUp import pygame_setup
from sys import exit
from Screen import Screen
from PygameSetUp import pg
from Player import Player1


def main():
    screen = Screen()
    pygame_setup()
    screen.screen_setup()
    p1 = Player1(screen)
    p2 = Player2(screen)

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:

                    p1.draw_symbol()
                    pg.display.update()
                    pass


if "__name__" == main():
    main()
