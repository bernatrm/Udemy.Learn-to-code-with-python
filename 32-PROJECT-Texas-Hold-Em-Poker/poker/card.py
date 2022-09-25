class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")

    RANKS = (
                "2","3","4","5","6","7","8","9","10",
                "Jack","Queen","King","Ace"
            )

    @classmethod
    def create_standard_52_cards(cls):
        return [
            cls(rank = rank, suit= suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

    def __init__(self, rank, suit) -> None:
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")

        self.rank = rank
        self.rank_index = self.RANKS.index(rank)
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other: object) -> bool:
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other: object) -> bool:
        return self.rank_index < other.rank_index