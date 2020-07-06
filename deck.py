import random
from typing import List
from card import Card, Suit, Rank


class Deck:
    def __init__(self):
        self._cards = []
        self.number_of_cards_left = 0
        self.reset_deck()

    @classmethod
    def __build_deck(cls) -> List[Card]:
        cards = []
        for suit in Suit:
            for rank in Rank:
                cards.append(Card(suit, rank))
        random.shuffle(cards)
        return cards

    def get_cards(self) -> List[Card]:
        return self._cards

    def get_num_of_cards(self) -> int:
        return len(self._cards)

    def reset_deck(self):
        self._cards = self.__build_deck()

    def draw_card(self) -> Card:
        if len(self._cards) == 0:
            raise ValueError("No more cards in the deck")
        return self._cards.pop()
