class GameRound():
    def __init__(self, deck, players) -> None:
        self.deck = deck
        self.players = players

    def play(self):
        # Shuffle the deck
        self.deck.shuffle()
        # Hand out 2 cards to each player
        # Ask for wagers
        pass

