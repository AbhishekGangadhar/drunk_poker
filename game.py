from hand import Hand
from player import Player
from deck import Deck
from typing import List
from card import Card


class Game:
    def __init__(self, deck: Deck = Deck()):
        self._players = []
        self._hand_to_player = {}
        self._deck = deck
        self._game_setup()

    def _game_setup(self):
        self._players = []
        for i in range(1, 5):
            self._players.append(Player("Player {}".format(i)))

    def _deal_hand(self) -> Hand:
        return Hand.get_hand_from_cards([self._deck.draw_card() for _ in range(3)])

    def _process_tie_game(self, hands: List[Hand]) -> Player:
        print("Game is tied, Each player to draw cards until one of them get a higher card")
        game_drawn = True
        players = [self._hand_to_player[hand] for hand in hands]
        FIRST_CARD = 0
        SECOND_CARD = 1
        while game_drawn:
            print()
            print("Players Draw Cards...")
            print()
            card_to_player = {}
            cards = []
            for player in players:
                card = self._deck.draw_card()
                card_to_player[card] = player
                cards.append(card)
                print("{} drew card {}".format(player, card))
            cards = Card.sort_cards_by_rank(cards)
            if cards[FIRST_CARD].get_rank().value > cards[SECOND_CARD].get_rank().value:
                return card_to_player[cards[FIRST_CARD]]
            if self._deck.get_num_of_cards() < len(self._players):
                self._deck.reset_deck()
            print("Still a draw!!")

    @classmethod
    def _check_if_draw(cls, strongest_hand: Hand, hands: List[Hand]) -> bool:
        hands_count = 0
        for hand in hands:
            if (
                hand.get_hand_type() == strongest_hand.get_hand_type()
                and hand.get_hand_type_rank() == strongest_hand.get_hand_type_rank()
                and hand.get_high_card_rank() == strongest_hand.get_high_card_rank()
                and hand.get_cards_value() == strongest_hand.get_cards_value()
            ):
                hands_count += 1
        return hands_count > 1

    def _process_hands(self) -> Player:
        FIRST_HAND = 0
        hands = list(self._hand_to_player.keys())
        hands = Hand.sort_hands(hands)
        strongest_hand = hands[FIRST_HAND]
        if self._check_if_draw(strongest_hand, hands):
            return self._process_tie_game(hands)
        return self._hand_to_player[strongest_hand]

    def run(self):
        print()
        print(" *********************** Welcome to Drunk Poker! *********************** ")
        print()
        self._game_setup()
        for player in self._players:
            hand = self._deal_hand()
            self._hand_to_player[hand] = player
            cards_string = ", ".join([str(card) for card in hand.get_cards()])
            print("{} was dealt with cards: {}".format(player.get_name(), cards_string))
        player = self._process_hands()
        print()
        print("Winner: {}!!!".format(player.get_name()))
        print()
        print(" *********************** Bye! *********************** ")
        print()
