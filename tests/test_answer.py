# pylint: disable-all
import unittest

from main import answer

class TestAnswer(unittest.TestCase):
    def test_answer_to_number_of_the_beast(self):
        expected = 42
        self.assertEqual(answer(666), expected)

    def test_answer_to_everything(self):
        expected = 42
        self.assertEqual(answer("Everything"), expected)

    def test_answer_to_nothing(self):
        expected = 42
        self.assertEqual(answer(), expected)
