from poker.card import Card
from poker.deck import Deck
from poker.game_round import GameRound
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()
hand3 = Hand()

player1 = Player(name= "Bernat", hand= hand1) 
player2 = Player(name= "Bobby", hand= hand2)
player3 = Player(name= "Llorenç", hand= hand3)
players = [player1, player2, player3]

game_round = GameRound(deck=deck, players=players)
game_round.play()

for player in players:
    print(f"{player.name} revices a {player.hand}.")
    index, hand_name, hand_cards = player.best_hand()
    hand_card_strings = [str(card) for card in hand_cards]
    hand_card_strings = " and ".join(hand_card_strings)
    print(F"{player.name} has a {hand_name} with a {hand_card_strings}.")

winning_player = max(players)

print(f"The winner es {winning_player.name}.")