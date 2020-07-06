import unittest
from unittest import TestCase
from card import Card, Suit, Rank


class TestCards(TestCase):
    def test(self):
        ace_of_spades = Card(Suit.SPADES, Rank.ACE)
        self.assertEqual(Suit.SPADES, ace_of_spades.get_suit())
        self.assertEqual(Rank.ACE, ace_of_spades.get_rank())
        self.assertEqual("ACE of SPADES", ace_of_spades.string())
        self.assertEqual(1, ace_of_spades.get_rank().value)

        two_of_hearts = Card(Suit.HEARTS, Rank.TWO)
        self.assertEqual(Suit.HEARTS, two_of_hearts.get_suit())
        self.assertEqual(Rank.TWO, two_of_hearts.get_rank())
        self.assertEqual("TWO of HEARTS", two_of_hearts.string())
        self.assertEqual(2, two_of_hearts.get_rank().value)

        seven_of_clubs = Card(Suit.CLUBS, Rank.SEVEN)
        self.assertEqual(Suit.CLUBS, seven_of_clubs.get_suit())
        self.assertEqual(Rank.SEVEN, seven_of_clubs.get_rank())
        self.assertEqual("SEVEN of CLUBS", seven_of_clubs.string())
        self.assertEqual(7, seven_of_clubs.get_rank().value)

        jack_of_diamonds = Card(Suit.DIAMONDS, Rank.JACK)
        self.assertEqual(Suit.DIAMONDS, jack_of_diamonds.get_suit())
        self.assertEqual(Rank.JACK, jack_of_diamonds.get_rank())
        self.assertEqual("JACK of DIAMONDS", jack_of_diamonds.string())
        self.assertEqual(11, jack_of_diamonds.get_rank().value)


if __name__ == '__main__':
    unittest.main()
