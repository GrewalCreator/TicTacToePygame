import pygame as pg


def pygame_setup():
    check_errors = pg.init()
    if check_errors[1] > 0:
        print("Error", check_errors[1])
    else:
        print("Game Successfully Initialized")
