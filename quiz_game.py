#! python3

'''Questionare game developed as an assignement in DAT120, a university course at UiS

Author: Jacob Dieset'''

import random

class Question:
    def __init__(self, question: str, alternatives: list, correct: int):
        self.question = question
        self.alternatives = alternatives
        self.correct = correct + 1

    def correct_answer_txt(self):
        print(f'The correct answer is: {self.alternatives[self.correct-1]}')

    def check(self, answer):
        if answer == self.correct:
            print('Correct answer!\n')
        else:
            print('Wrong answer.\n')

    def shuffle_alt(self):
        answer = self.alternatives[self.correct - 1]
        random.shuffle(self.alternatives)
        self.correct = self.alternatives.index(answer) + 1

    def __str__(self):
        self.shuffle_alt()
        return f'{self.question}\n' + f'Alternatives:\n1:\t{self.alternatives[0]}\n2:\t{self.alternatives[1]}\n3:\t{self.alternatives[2]}\n4:\t{self.alternatives[3]}'


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0




if __name__ == '__main__':
    questions = list()

    with open('sporsmaalsfil.txt', 'r', encoding='utf8') as file:
        for line in file:
            list = line.split(':')
            alts = list[2].strip('\n []')
            alts = alts.split(', ')
            questions.append(Question(list[0], alts, int(list[1])))

    for question in questions:
        try:
            print(question)
            answer = int(input('Input answer alternative: '))
            question.check(answer)
        except IndexError:
            pass