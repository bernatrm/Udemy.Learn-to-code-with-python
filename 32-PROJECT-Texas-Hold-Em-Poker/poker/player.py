class Player():
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def best_hand(self) -> str:
        return self.hand.best_rank()

    def add_cards(self, cards) -> None:
        self.hand.add_cards(cards)

    def wants_to_fold(self) -> bool:
        return False


    