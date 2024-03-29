from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator, 
    HighCardValidator, 
    NoCardsValidator
)

class Hand():
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator, 
        HighCardValidator, 
        NoCardsValidator       
    )

    def __init__(self) -> None:
        self.cards = []
    
    def __repr__(self) -> str:
        cards_as_strings = [str(card) for card in self.cards]        
        return ", ".join(cards_as_strings)

    def add_cards(self, cards) -> None:
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def best_rank(self) -> str:
        for index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(cards= self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())