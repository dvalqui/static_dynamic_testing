import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

    def test_check_for_ace_false(self):
        card = Card('clubs', 7)
        actual = CardGame.check_for_ace(self, card)
        self.assertFalse(actual)

    def test_check_for_ace_true(self):
        card = Card('clubs', 1)  # Arrange
        actual = CardGame.check_for_ace(self, card)  # Act
        self.assertTrue(actual)  # Assert

    def test_highest_card_first_higher(self):
        card1 = Card('clubs', 9)
        card2 = Card('clubs', 3)

        actual = CardGame.highest_card(self, card1, card2)

        self.assertEqual(card1, actual)  # Assert

    def test_highest_card_second_higher(self):
        card1 = Card('clubs', 2)
        card2 = Card('clubs', 10)

        actual = CardGame.highest_card(self, card1, card2)
        self.assertEqual(card2, actual)

#Expected and Actual
