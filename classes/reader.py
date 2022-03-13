import pygame as py

from classes.answer import Answer
from classes.question import Question
from constants import *


class Reader:

    def __init__(self):
        questions = self.extract_question()
        answers = self.extract_answers()
        self.questions = []
        for i in range(len(questions)):
            question = Question(questions[i], [Answer(answers[i][0], 0), Answer(answers[i][1], 1), Answer(answers[i][2], 2),
                                 Answer(answers[i][3], 3)], int(answers[i][4]))
            self.questions.append(question)


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

