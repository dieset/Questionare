#! python3

import unittest
from quiz_game import Question

class TestQuiz(unittest.TestCase):
    def test_question_check(self):
        q1 = Question('Hvilken farge har himmelen?', ['Grønn', 'Gul', 'Blå'], 2)
        self.assertFalse(q1.check(1))
        self.assertTrue(q1.check(3))
        self.assertFalse(q1.check(2))

    def test_correct_txt(self):
        q2 = Question('''"Hjernen" til en datamaskin kalles?''', ['RAM', 'CPU', 'Data', 'Harddisk'], 1)
        self.assertEqual(q2.correct_answer_txt(), q2.alternatives[q2.correct-1])
        self.assertNotEqual(q2.correct_answer_txt(), q2.alternatives[0])
        self.assertNotEqual(q2.correct_answer_txt(), q2.alternatives[2])
        self.assertNotEqual(q2.correct_answer_txt(), q2.alternatives[3])


if __name__ == '__main__':
    unittest.main()