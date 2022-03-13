import pygame as py

from classes.reader import Reader
from constants import *


class Manager:
    def __init__(self, screen):
        self.screen = screen
        self.reader = Reader()
        img = py.image.load(BACKGROUND_PATH)
        self.background_img = py.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        img = py.image.load(TIMER_PATH)
        self.timer_img = py.transform.scale(img, (TIMER_WIDTH, TIMER_HEIGHT))
        self.mode = 'home'
        self.time_left = TIME_FOR_QUESTION
        self.questions_left = self.reader.questions
        self.score = 0

    def show_background(self):
        self.screen.blit(self.background_img, (0, 0))

    def show_start_button(self):
        py.draw.rect(self.screen, GREEN_COLOR, (START_BUTTON_POS_X, START_BUTTON_POS_Y,
                                                START_BUTTON_WIDTH, START_BUTTON_HEIGHT))
        font = py.font.SysFont(START_BUTTON_TEXT_FONT, START_BUTTON_TEXT_SIZE)
        self.screen.blit(font.render(START_BUTTON_TEXT, True, BLACK_COLOR), (START_BUTTON_POS_X, START_BUTTON_POS_Y))
        font = py.font.SysFont(WELCOME_MSG_FONT, WELCOME_MSG_SIZE)
        self.screen.blit(font.render(WELCOME_MSG, True, BLACK_COLOR), (WELCOME_MSG_POS_X, WELCOME_MSG_POS_Y))

    def click_start(self, pos):
        if START_BUTTON_POS_X <= pos[0] <= START_BUTTON_POS_X + START_BUTTON_WIDTH and START_BUTTON_POS_Y <= pos[1] <= START_BUTTON_POS_Y + START_BUTTON_HEIGHT:
            return True
        return False

    def show_question(self):
        font = py.font.SysFont(QUESTION_FONT, QUESTION_SIZE)
        self.screen.blit(font.render(self.questions_left[0].text, True, BLACK_COLOR), (QUESTION_POS_X, QUESTION_POS_Y))

    def show_answers(self):
        font = py.font.SysFont(ANSWER_FONT, ANSWER_SIZE)
        for i in range(4):
            py.draw.rect(self.screen, RED_COLOR, (ANSWER_INDEXED_POS[i][0], ANSWER_INDEXED_POS[i][1],
                                                    ANSWER_RECT_WIDTH, ANSWER_RECT_HEIGHT))
            self.screen.blit(font.render(self.questions_left[0].answers[i].text, True, BLACK_COLOR),
                             (ANSWER_INDEXED_POS[i][0], ANSWER_INDEXED_POS[i][1]))

    def show_time(self):
        self.screen.blit(self.timer_img, (TIMER_POS_X, TIMER_POS_Y))
        font = py.font.SysFont(TIME_FONT, TIME_SIZE)
        self.screen.blit(font.render(str(self.time_left), True, BLACK_COLOR),
                         (TIME_POS_X, TIME_POS_Y))
        self.time_left = round(self.time_left - 0.01, 2)

    def clicked_ans_i(self, i, pos):
        if ANSWER_INDEXED_POS[i][0] <= pos[0] <= ANSWER_INDEXED_POS[i][0] + ANSWER_RECT_WIDTH and ANSWER_INDEXED_POS[i][1] <= pos[1] <= ANSWER_INDEXED_POS[i][1] + ANSWER_RECT_HEIGHT:
            return True
        return False

    def show_score(self):
        font = py.font.SysFont(SCORE_TEXT_FONT, SCORE_TEXT_SIZE)
        self.screen.blit(font.render(SCORE_TEXT + str(round(self.score, 2)), True, BLACK_COLOR),
                         (SCORE_POS_X, SCORE_POS_Y))

    def choose_ans(self, i):
        if self.questions_left[0].curr_ans_index == i:
            self.score += self.time_left
        self.questions_left = self.questions_left[1:]
        self.time_left = TIME_FOR_QUESTION
        if len(self.questions_left) == 0:
            self.mode = 'done'

    def show_end_message(self):
        font = py.font.SysFont(END_TEXT_FONT, END_TEXT_SIZE)
        self.screen.blit(font.render(END_TEXT, True, BLACK_COLOR),
                         (END_TEXT_POS_X, END_TEXT_POS_Y))

    def check_times_up(self):
        if self.time_left <= 0.5:
            self.choose_ans(4)
