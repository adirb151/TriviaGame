import pygame as py

from classes.manager import Manager
from constants import *

py.init()
screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = py.display.set_mode(screen_size)
clock = py.time.Clock()

manager = Manager(screen)
manager.show_background()

py.display.flip()


def is_finished():
    finished = False
    for event in py.event.get():
        if event.type == py.QUIT:
            finished = True
    return finished


while not is_finished():
    py.display.flip()
    clock.tick(60)

py.quit()




