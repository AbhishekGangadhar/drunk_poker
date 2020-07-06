import unittest
from unittest import TestCase
from deck import Deck
from card import Rank, Suit
from copy import deepcopy


class TestDeck(TestCase):
    def test_build_deck(self):
        deck = Deck()
        cards = deck.get_cards()
        self.assertEqual(52, len(cards))
        for rank in Rank:
            self.assertEqual(4, len(list(filter(lambda x: x.get_rank() == rank, cards))))
        for suit in Suit:
            self.assertEqual(13, len(list(filter(lambda x: x.get_suit() == suit, cards))))

    def test_draw_card(self):
        deck = Deck()
        cards = deck.get_cards()
        original_cards = deepcopy(cards)
        self.assertEqual(52, deck.get_num_of_cards())
        drawn_cards = []
        for _ in range(20):
            drawn_cards.append(str(deck.draw_card()))
        self.assertEqual(32, deck.get_num_of_cards())
        self.assertEqual(20, len(list(filter(lambda x: str(x) in drawn_cards, original_cards))))
        self.assertEqual(0, len(list(filter(lambda x: str(x) in drawn_cards, cards))))

    def test_reset_deck(self):
        deck = Deck()
        self.assertEqual(52, deck.get_num_of_cards())
        for _ in range(10):
            deck.draw_card()
        self.assertEqual(42, deck.get_num_of_cards())
        deck.reset_deck()
        self.assertEqual(52, deck.get_num_of_cards())


if __name__ == '__main__':
    unittest.main()
