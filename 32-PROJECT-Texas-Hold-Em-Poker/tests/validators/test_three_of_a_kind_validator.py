import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.five_of_clubs    = Card(rank= "5", suit= "Clubs")
        self.king_of_clubs    = Card(rank= "King", suit= "Clubs")
        self.king_of_hearts   = Card(rank= "King", suit= "Hearts")
        self.king_of_diamonds = Card(rank= "King", suit= "Diamonds")
        self.ace_of_spades    = Card(rank= "Ace", suit= "Spades")

        self.cards = [
            self.five_of_clubs,
            self.king_of_clubs,
            self.king_of_hearts,
            self.king_of_diamonds,
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_exactly_three_of_the_same_rank(self):
        validator = ThreeOfAKindValidator(cards= self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_colletion_of_cards_that_have_exactly_one_three_of_the_same_rank(self):
        validator = ThreeOfAKindValidator(cards= self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs, 
                self.king_of_hearts, 
                self.king_of_diamonds
            ]
        )