class Player():
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def best_hand(self):
        return self.hand.best_rank()