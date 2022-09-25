class GameRound():
    def __init__(self, deck, players) -> None:
        self.deck = deck
        self.players = players

    def play(self):
        # Shuffle the deck
        self._shuffle_deck()
        
        # Assign two cards to every player
        self._deal_initial_two_cards_to_each_player()

        # Ask for wagers

    def _shuffle_deck(self):
        self.deck.shuffle()

    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)