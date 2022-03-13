import pygame as py

from classes.reader import Reader
from constants import *


class Manager:
    def __init__(self, screen):
        self.screen = screen
        self.reader = Reader()
        img = py.image.load(BACKGROUND_PATH)
        self.img = py.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.mode = 'home'

    def show_background(self):
        self.screen.blit(self.img, (0, 0))

    def show_start_button(self):
        py.draw.rect(self.screen, GREEN_COLOR, (START_BUTTON_POS_X, START_BUTTON_POS_Y,
                                                START_BUTTON_WIDTH, START_BUTTON_HEIGHT))
        font = py.font.SysFont()
