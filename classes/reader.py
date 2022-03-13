import pygame as py

from constants import *


class Reader:

    def __init__(self):
        self.question = self.extract_question()
        self.answers = self.extract_answers()


    def extract_question(self):
        question_file = open(QUESTIONS_FILE_PATH, 'r')
        questions = question_file.readlines()
        for i in range(len(questions)):
            questions[i] = questions[i].strip()
        question_file.close()
        return questions

    def extract_answers(self):
        answers_file = open(ANSWERS_FILE_PATH, 'r')
        answers = answers_file.readlines()
        for i in range(len(answers)):
            answers[i] = answers[i].strip().split(',')
        answers_file.close()
        return answers

