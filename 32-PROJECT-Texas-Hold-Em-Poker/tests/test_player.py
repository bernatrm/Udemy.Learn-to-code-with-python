from ipaddress import NetmaskValueError
import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.player import Player

class PlayerTest(unittest.TestCase):
    def test_store_name_and_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Bernat", hand = mock_hand)
        self.assertEqual(player.name, "Bernat")
        self.assertEqual(player.hand, mock_hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"

        player = Player(name = "Bernat", hand = mock_hand)

        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )

        mock_hand.best_rank.assert_called()
    
    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name= "Kimberly", hand= mock_hand)

        cards = [
            Card(rank= "Ace", suit= "Spades"),
            Card(rank= "Queen", suit= "Diamonds")
        ]

        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)
