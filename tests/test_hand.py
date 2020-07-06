import unittest
from unittest import TestCase
from hand import Hand, HandType
from card import Card, Suit, Rank

_ACE_OF_SPACES = Card(Suit.SPADES, Rank.ACE)
_ACE_OF_CLUBS = Card(Suit.SPADES, Rank.ACE)
_ACE_OF_HEARTS = Card(Suit.SPADES, Rank.ACE)

_KING_OF_CLUBS = Card(Suit.CLUBS, Rank.KING)
_QUEEN_OF_CLUBS = Card(Suit.CLUBS, Rank.QUEEN)

_TWO_OF_SPACES = Card(Suit.SPADES, Rank.TWO)
_THREE_OF_CLUBS = Card(Suit.CLUBS, Rank.THREE)
_FOUR_OF_HEARTS = Card(Suit.HEARTS, Rank.FOUR)

_SEVEN_OF_SPACES = Card(Suit.SPADES, Rank.SEVEN)
_SEVEN_OF_CLUBS = Card(Suit.SPADES, Rank.SEVEN)
_SEVEN_OF_HEARTS = Card(Suit.SPADES, Rank.SEVEN)


class TestHand(TestCase):
    def test_sets(self):
        set_of_aces = [_ACE_OF_SPACES, _ACE_OF_CLUBS, _ACE_OF_HEARTS]
        hand = Hand.get_hand_from_cards(set_of_aces)
        self.assertEqual(HandType.SET, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_rank_high_card())

        set_of_sevens = [_SEVEN_OF_SPACES, _SEVEN_OF_CLUBS, _SEVEN_OF_HEARTS]
        hand = Hand.get_hand_from_cards(set_of_sevens)
        self.assertEqual(HandType.SET, hand.get_hand_type())
        self.assertEqual(Rank.SEVEN, hand.get_hand_rank_high_card())

    def test_straights(self):
        straight_from_1_to_3 = [_TWO_OF_SPACES, _ACE_OF_SPACES, _THREE_OF_CLUBS]
        hand = Hand.get_hand_from_cards(straight_from_1_to_3)
        self.assertEqual(HandType.STRAIGHT, hand.get_hand_type())
        self.assertEqual(Rank.THREE, hand.get_hand_rank_high_card())

        straight_from_2_to_4 = [_TWO_OF_SPACES, _FOUR_OF_HEARTS, _THREE_OF_CLUBS]
        hand = Hand.get_hand_from_cards(straight_from_2_to_4)
        self.assertEqual(HandType.STRAIGHT, hand.get_hand_type())
        self.assertEqual(Rank.FOUR, hand.get_hand_rank_high_card())

        straight_ace_king_queen = [_ACE_OF_SPACES, _KING_OF_CLUBS, _QUEEN_OF_CLUBS]
        hand = Hand.get_hand_from_cards(straight_ace_king_queen)
        self.assertEqual(HandType.STRAIGHT, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_rank_high_card())

    def test_pairs(self):
        pair_of_7s_with_ace_high = [_SEVEN_OF_CLUBS, _SEVEN_OF_HEARTS, _ACE_OF_SPACES]
        hand = Hand.get_hand_from_cards(pair_of_7s_with_ace_high)
        self.assertEqual(HandType.PAIR, hand.get_hand_type())
        self.assertEqual(Rank.SEVEN, hand.get_hand_rank_high_card())
        self.assertEqual(Rank.ACE, hand.get_high_card_rank())

        pair_of_aces_with_king_high = [_KING_OF_CLUBS, _ACE_OF_HEARTS, _ACE_OF_SPACES]
        hand = Hand.get_hand_from_cards(pair_of_aces_with_king_high)
        self.assertEqual(HandType.PAIR, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_rank_high_card())
        self.assertEqual(Rank.KING, hand.get_high_card_rank())

    def test_high_card(self):
        seven_high = [_SEVEN_OF_CLUBS, _TWO_OF_SPACES, _THREE_OF_CLUBS]
        hand = Hand.get_hand_from_cards(seven_high)
        self.assertEqual(HandType.HIGH_CARD, hand.get_hand_type())
        self.assertEqual(Rank.SEVEN, hand.get_hand_rank_high_card())
        self.assertEqual(Rank.SEVEN, hand.get_high_card_rank())

        ace_high = [_SEVEN_OF_CLUBS, _TWO_OF_SPACES, _ACE_OF_SPACES]
        hand = Hand.get_hand_from_cards(ace_high)
        self.assertEqual(HandType.HIGH_CARD, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_rank_high_card())
        self.assertEqual(Rank.ACE, hand.get_high_card_rank())

    def test_pre_check(self):
        self.assertRaisesRegex(ValueError, "Length of the cards need to be 3, given: 0 cards",
                               Hand.get_hand_from_cards, [])
        self.assertRaisesRegex(ValueError, "Length of the cards need to be 3, given: 2 cards",
                               Hand.get_hand_from_cards, [_TWO_OF_SPACES, _ACE_OF_SPACES])


if __name__ == '__main__':
    unittest.main()
