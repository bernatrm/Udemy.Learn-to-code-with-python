class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self) -> str:                # Human friendly
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:               # Technical friendly, if __str__ is not defined, __repr__ will be used on call print(object)
        return f'Card("{self.rank}", "{self.suit}")'

c = Card("Ace", "Spades")
print(c)
print(repr(c))

print(c.__str__())
print(c.__repr__())