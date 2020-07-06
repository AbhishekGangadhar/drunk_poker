from hand import Hand
from player import Player
from deck import Deck
from typing import List
from card import Card
from collections import Counter


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

    def _process_hands(self) -> Player:
        FIRST_ELEMENT = 0

        # Checking if there is only one hand with best hand type
        hands = sorted(self._hand_to_player.keys(), key=lambda x: x.get_hand_type().value, reverse=True)
        best_hand_rank = hands[FIRST_ELEMENT].get_hand_type().value
        hands = list(filter(lambda x: x.get_hand_type().value == best_hand_rank, hands))
        if len(hands) == 1:
            return self._hand_to_player[hands[FIRST_ELEMENT]]

        # Checking if there is only one hand with best hand type rank
        hands = sorted(hands, key=lambda x: x.get_hand_type_rank().value, reverse=True)
        best_hand_type_rank = hands[FIRST_ELEMENT].get_hand_type_rank().value
        hands = list(filter(lambda x: x.get_hand_type_rank().value == best_hand_type_rank, hands))
        if len(hands) == 1:
            return self._hand_to_player[hands[FIRST_ELEMENT]]

        # Checking for the best high card hand
        hands_to_cards = {}
        for hand in hands:
            hands_to_cards[hand] = Card.sort_cards_by_rank(hand.get_cards())

        for _ in range(3):
            rank_value_counter = Counter([cards[FIRST_ELEMENT].get_rank().value for cards in hands_to_cards.values()])
            best_high_card_rank_val = max(rank_value_counter.keys())

            if rank_value_counter[best_high_card_rank_val] == 1:
                for hand, cards in hands_to_cards.items():
                    if cards[FIRST_ELEMENT].get_rank().value == best_high_card_rank_val:
                        return self._hand_to_player[hand]
            else:
                hands_to_be_deleted = []
                for hand, cards in hands_to_cards.items():
                    if cards[FIRST_ELEMENT].get_rank().value != best_high_card_rank_val:
                        hands_to_be_deleted.append(hand)
                    else:
                        cards.pop(0)
                for hand in hands_to_be_deleted:
                    del hands_to_cards[hand]
        return self._process_tie_game(hands)

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


