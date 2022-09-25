import random
class Deck():
    def __init__(self) -> None:
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def shuffle(self):
        random.shuffle(self.cards)
