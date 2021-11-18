#! python3
'''
Questionare game developed as an assignement in DAT120, a university course at UiS

Author: Jacob Dieset
'''

import random

class Question:
    def __init__(self, question: str, alternatives: list, correct: int):
        self.question = question
        self.alternatives = alternatives
        self.correct = correct + 1

    def correct_answer_txt(self):
        print(f'The correct answer is: {self.alternatives[self.correct-1]}')
        return self.alternatives[self.correct-1]

    def check(self, answer: int):
        if answer == self.correct:
            print('Correct answer!\n')
            return True
        else:
            print('Wrong answer.\n')
            return False

    def shuffle_alt(self):
        answer = self.alternatives[self.correct - 1]
        random.shuffle(self.alternatives)
        self.correct = self.alternatives.index(answer) + 1

    def __str__(self) -> str:
        self.shuffle_alt()
        part1 = f'{self.question}\nAlternatives:\n'
        part2 = [f'{index+1}:\t{alt}\n' for index, alt in enumerate(self.alternatives)]
        return part1 + ''.join(part2)


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.answer = None

    def give_answer(self) -> int:
        self.answer = int(input(f'{self.name}, choose your answer: '))
        return (self.answer)

    def check_correct(self, question: Question):
        if question.correct == self.answer:
            self.score += 1

def create_player_list(empty_list: list):
    number_of_players = int(input('Input number of players: '))
    for i in range(number_of_players):
        player = input('Input player name: ')
        if player != '':
            empty_list.append(Player(player))
        else:
            break

if __name__ == '__main__':
    question_list = list()
    player_list = list()

    with open('sporsmaalsfil.txt', 'r', encoding='utf8') as file:
        for line in file:
            list = line.split(':')
            alts = list[2].strip('\n []')
            alts = alts.split(', ')
            question_list.append(Question(list[0], alts, int(list[1])))

    print('Welcome to the Questionare!\nWho is playing?')

    '''number_of_players = int(input('Input number of players: '))
    for i in range(number_of_players):
        player = input('Input player name: ')
        if player != '':
            players.append(Player(player))
        else:
            break'''

    create_player_list(player_list)

    for question in question_list:
        print(question)
        for player in player_list:
            player.give_answer()
            player.check_correct(question)
        for player in player_list:
            question.check(player.answer)
        question.correct_answer_txt()
        input('Press enter to continue...')
        print()

    player_list.sort(key=lambda x: x.score, reverse=True)

    for player in player_list:
        print(f'Final score for {player.name} is {player.score}')