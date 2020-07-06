from collections import Counter
from enum import Enum
from typing import List

from card import Card, Rank


class HandType(Enum):
    SET = 4
    STRAIGHT = 3
    PAIR = 2
    HIGH_CARD = 1


class Hand:
    def __init__(self, cards: List[Card], hand_type: HandType, hand_type_rank: Rank, high_card_rank: Rank):
        self.__hand_type = hand_type
        self.__hand_rank_high_card = hand_type_rank
        self.__high_card_rank = high_card_rank
        self.__cards = cards

    def get_hand_type(self) -> HandType:
        return self.__hand_type

    def get_hand_rank_high_card(self) -> Rank:
        return self.__hand_rank_high_card

    def get_high_card_rank(self) -> Rank:
        return self.__high_card_rank

    def get_cards(self) -> List[Card]:
        return self.__cards

    @staticmethod
    def get_hand_from_cards(cards: List[Card]):
        if len(cards) != 3:
            raise ValueError("Length of the cards need to be 3, given: {} cards".format(len(cards)))
        FIRST_CARD = 0
        cards = sorted(cards, key=lambda x: x.get_rank().value, reverse=True)
        card_rank_values = [card.get_rank().value for card in cards]
        if len(set(card_rank_values)) == 1:
            return Hand(cards, HandType.SET, cards[FIRST_CARD].get_rank(), cards[FIRST_CARD].get_rank())

        if all([card_rank_values[i] - 1 == card_rank_values[i + 1] for i in range(2)]) or {1, 12, 13} == set(card_rank_values):
            high_card_rank = cards[FIRST_CARD].get_rank()
            if {1, 12, 13} == set(card_rank_values):
                high_card_rank = Rank.ACE
            return Hand(cards, HandType.STRAIGHT, high_card_rank, high_card_rank)

        rank_counter = Counter([card.get_rank() for card in cards])
        for rank, count in rank_counter.items():
            if count == 2:
                unique_values = set(rank_counter.keys())
                unique_values.remove(rank)
                high_card = list(unique_values)[FIRST_CARD]
                return Hand(cards, HandType.PAIR, rank, high_card)

        high_card_rank = cards[FIRST_CARD].get_rank()
        if Rank.ACE in [card.get_rank() for card in cards]:
            high_card_rank = Rank.ACE
        return Hand(cards, HandType.HIGH_CARD, high_card_rank, high_card_rank)
