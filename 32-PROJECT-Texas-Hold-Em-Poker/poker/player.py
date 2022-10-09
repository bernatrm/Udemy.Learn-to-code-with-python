class Player():
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def __gt__(self, other: object) -> bool:
        current_player_best_validator_index = self.best_hand()[0]
        other_player_best_validator_index = other.best_hand()[0]

        return current_player_best_validator_index < other_player_best_validator_index

    def best_hand(self) -> str:
        return self.hand.best_rank()

    def add_cards(self, cards) -> None:
        self.hand.add_cards(cards)

    def wants_to_fold(self) -> bool:
        return False



    