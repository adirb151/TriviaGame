import pygame as py

from constants import *


class Question:
    def __init__(self, text, answers, curr_ans_index):
        self.text = text
        self.answers = answers
        self.curr_ans_index = curr_ans_index

