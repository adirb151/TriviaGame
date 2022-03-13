import pygame as py

from constants import *

class Manager:
    def __init__(self, screen):
        self.screen = screen
        img = py.image.load(BACKGROUP_PATH)
        self.img = py.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def show_background(self):
        self.screen.blit(self.img, (0, 0))
