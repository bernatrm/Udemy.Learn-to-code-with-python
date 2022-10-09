from poker.validators import FiveCardRanksInARowValidator

class StraightFlushValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards) -> None:
        self.cards = cards
        self.name = "Straight Flush"
    
    def is_valid(self):
        for five_cards in self._collections_of_five_straight_cards_in_a_row:
            unique_suits_in_next_five_cards = { card.suit for card in five_cards }
            if len(unique_suits_in_next_five_cards) == 1:
                return True

        return False

    def valid_cards(self):
        return self._straight_flush_card_batches[-1]

    #[[All Clubs], [Clubs, Diamonds]]
    #[[3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
    #[[3, 4, 5, 6, 7]]

    @property
    def _straight_flush_card_batches(self):
        #Filter List to return only that one matching our condition
        return [
                five_cards
                for five_cards in self._collections_of_five_straight_cards_in_a_row
                if len({ card.suit for card in five_cards }) == 1
        ]