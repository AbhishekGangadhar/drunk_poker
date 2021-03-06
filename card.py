from enum import Enum


class Suit(Enum):
    HEARTS = "HEARTS"
    DIAMONDS = "DIAMONDS"
    SPADES = "SPADES"
    CLUBS = "CLUBS"


class Rank(Enum):
    ACE = 1
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.__suit = suit
        self.__rank = rank

    def __str__(self) -> str:
        return f"{self.__rank.name} of {self.__suit.value}"

    def get_suit(self) -> Suit:
        return self.__suit

    def get_rank(self) -> Rank:
        return self.__rank

    @staticmethod
    def sort_cards_by_rank(cards):
        aces = list(filter(lambda x: x.get_rank() == Rank.ACE, cards))
        non_ace_cards = list(filter(lambda x: x.get_rank() != Rank.ACE, cards))
        non_ace_cards = sorted(non_ace_cards, key=lambda x: x.get_rank().value, reverse=True)
        return aces + non_ace_cards
