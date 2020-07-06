import unittest
from unittest import TestCase
from card import Card, Suit, Rank

_ACE_OF_SPADES = Card(Suit.SPADES, Rank.ACE)
_TWO_OF_HEARTS = Card(Suit.HEARTS, Rank.TWO)
_SEVEN_OF_CLUBS = Card(Suit.CLUBS, Rank.SEVEN)
_JACK_OF_DIAMONDS = Card(Suit.DIAMONDS, Rank.JACK)


class TestCards(TestCase):
    def test_cards(self):
        self.assertEqual(Suit.SPADES, _ACE_OF_SPADES.get_suit())
        self.assertEqual(Rank.ACE, _ACE_OF_SPADES.get_rank())
        self.assertEqual("ACE of SPADES", str(_ACE_OF_SPADES))
        self.assertEqual(1, _ACE_OF_SPADES.get_rank().value)

        self.assertEqual(Suit.HEARTS, _TWO_OF_HEARTS.get_suit())
        self.assertEqual(Rank.TWO, _TWO_OF_HEARTS.get_rank())
        self.assertEqual("TWO of HEARTS", str(_TWO_OF_HEARTS))
        self.assertEqual(2, _TWO_OF_HEARTS.get_rank().value)

        self.assertEqual(Suit.CLUBS, _SEVEN_OF_CLUBS.get_suit())
        self.assertEqual(Rank.SEVEN, _SEVEN_OF_CLUBS.get_rank())
        self.assertEqual("SEVEN of CLUBS", str(_SEVEN_OF_CLUBS))
        self.assertEqual(7, _SEVEN_OF_CLUBS.get_rank().value)

        self.assertEqual(Suit.DIAMONDS, _JACK_OF_DIAMONDS.get_suit())
        self.assertEqual(Rank.JACK, _JACK_OF_DIAMONDS.get_rank())
        self.assertEqual("JACK of DIAMONDS", str(_JACK_OF_DIAMONDS))
        self.assertEqual(11, _JACK_OF_DIAMONDS.get_rank().value)

    def test_sort_cards_by_rank(self):
        cards = [_TWO_OF_HEARTS, _SEVEN_OF_CLUBS, _JACK_OF_DIAMONDS]
        sorted_cards = Card.sort_cards_by_rank(cards)
        self.assertEqual([_JACK_OF_DIAMONDS, _SEVEN_OF_CLUBS, _TWO_OF_HEARTS], sorted_cards)

        cards = [_TWO_OF_HEARTS, _ACE_OF_SPADES, _JACK_OF_DIAMONDS]
        sorted_cards = Card.sort_cards_by_rank(cards)
        self.assertEqual([_ACE_OF_SPADES, _JACK_OF_DIAMONDS, _TWO_OF_HEARTS], sorted_cards)


if __name__ == '__main__':
    unittest.main()
