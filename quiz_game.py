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
        part1 = f'{self.question}\nAlternatives:\n'
        part2 = [f'{index+1}:\t{alt}\n' for index, alt in enumerate(self.alternatives)]
        return part1 + ''.join(part2)


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.answer = None

    def give_answer(self):
        self.answer = int(input(f'{self.name}, choose your answer: '))
        return (self.answer)

    def check_correct(self, question):
        if question.correct == self.answer:
            self.score += 1

if __name__ == '__main__':
    questions = list()
    players = list()

    with open('sporsmaalsfil.txt', 'r', encoding='utf8') as file:
        for line in file:
            list = line.split(':')
            alts = list[2].strip('\n []')
            alts = alts.split(', ')
            questions.append(Question(list[0], alts, int(list[1])))

    print('Welcome to the Questionare!\nWho is playing?')

    enter_name = True
    while enter_name:
        player = input('Input player name: ')
        if player != '':
            players.append(Player(player))
        else:
            enter_name = False

    for question in questions:
        print(question)
        for player in players:
            player.give_answer()
            player.check_correct(question)
        for player in players:
            question.check(player.answer)
        question.correct_answer_txt()
        input('Press enter to continue:')
        print()

    for player in players:
        print(f'Final score for {player.name} is {player.score}')