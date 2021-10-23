#! python3

# import random # to use random on a list: random.shuffle(<list>)

class Question:
    def __init__(self, question: str, alternatives: list, correct: int):
        self.question = question
        self.alternatives = alternatives
        self.correct = correct

    def check(self, answer):
        if answer == self.correct:
            print('Correct answer!\n')
        else:
            print('Wrong answer, you moron.\n')

    def __str__(self):
        return f'{self.question}\n' + f'Alternatives:\n1:\t{self.alternatives[0]}\n2:\t{self.alternatives[1]}\n3:\t{self.alternatives[2]}\n4:\t{self.alternatives[3]}'

q = 'What is the Kings name?'
alt = ['Nils', 'Harald', 'Petter', 'Carl']
cor = 2

q2 = 'What is the Queens name?'
alt2 = ['Silje', 'Siri', 'Sara', 'Sonja']
cor2 = 4

question1 = Question(q, alt, cor)
print(question1)
answer = int(input('Input answer alternative: '))
question1.check(answer)

input('Press enter to continue:')

question2 = Question(q2, alt2, cor2)
print(question2)
answer = int(input('Input answer alternative: '))
question2.check(answer)