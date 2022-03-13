import pygame as py

from classes.manager import Manager
from constants import *

py.init()
screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = py.display.set_mode(screen_size)
clock = py.time.Clock()

manager = Manager(screen)
manager.show_background()
manager.show_start_button()

py.display.flip()


def is_finished():
    finished = False
    for event in py.event.get():
        if event.type == py.QUIT:
            finished = True
        if manager.mode == 'home':
            if event.type == py.MOUSEBUTTONDOWN:
                if manager.click_start(event.pos):
                    manager.mode = 'play'
        elif manager.mode == 'play':
            if event.type == py.MOUSEBUTTONDOWN:
                for i in range(4):
                    if manager.clicked_ans_i(i, event.pos):
                        manager.choose_ans(i)
            manager.check_times_up()
        else:
            pass
    return finished


while not is_finished():
    if manager.mode == 'home':
        manager.show_background()
        manager.show_start_button()
    elif manager.mode == 'play':
        manager.show_background()
        manager.show_question()
        manager.show_answers()
        manager.show_time()
        manager.show_score()
    else:
        manager.show_background()
        manager.show_end_message()
        manager.show_score()

    py.display.flip()
    clock.tick(60)

py.quit()




