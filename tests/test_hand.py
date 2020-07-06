import unittest
from unittest import TestCase
from hand import Hand, HandType
from card import Rank
from tests.utils import _ACE_OF_SPADES, _ACE_OF_CLUBS, _ACE_OF_HEARTS, _KING_OF_CLUBS, _QUEEN_OF_CLUBS, \
    _TWO_OF_SPADES, _THREE_OF_CLUBS, _FOUR_OF_HEARTS, _SEVEN_OF_SPADES, _SEVEN_OF_CLUBS, _SEVEN_OF_HEARTS

set_of_aces = [_ACE_OF_SPADES, _ACE_OF_CLUBS, _ACE_OF_HEARTS]
set_of_sevens = [_SEVEN_OF_SPADES, _SEVEN_OF_CLUBS, _SEVEN_OF_HEARTS]
straight_from_1_to_3 = [_TWO_OF_SPADES, _ACE_OF_SPADES, _THREE_OF_CLUBS]
straight_from_2_to_4 = [_TWO_OF_SPADES, _FOUR_OF_HEARTS, _THREE_OF_CLUBS]
straight_ace_king_queen = [_ACE_OF_SPADES, _KING_OF_CLUBS, _QUEEN_OF_CLUBS]
pair_of_aces_with_king_high = [_KING_OF_CLUBS, _ACE_OF_HEARTS, _ACE_OF_SPADES]
pair_of_7s_with_ace_high = [_SEVEN_OF_CLUBS, _SEVEN_OF_HEARTS, _ACE_OF_SPADES]
ace_high_seven_kicker = [_SEVEN_OF_CLUBS, _TWO_OF_SPADES, _ACE_OF_SPADES]
ace_high_four_kicker = [_FOUR_OF_HEARTS, _TWO_OF_SPADES, _ACE_OF_SPADES]
seven_high = [_SEVEN_OF_CLUBS, _TWO_OF_SPADES, _THREE_OF_CLUBS]


class TestHand(TestCase):
    def test_sets(self):
        hand = Hand.get_hand_from_cards(set_of_aces)
        self.assertEqual(HandType.SET, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_type_rank())

        hand = Hand.get_hand_from_cards(set_of_sevens)
        self.assertEqual(HandType.SET, hand.get_hand_type())
        self.assertEqual(Rank.SEVEN, hand.get_hand_type_rank())

    def test_straights(self):
        hand = Hand.get_hand_from_cards(straight_from_1_to_3)
        self.assertEqual(HandType.STRAIGHT, hand.get_hand_type())
        self.assertEqual(Rank.THREE, hand.get_hand_type_rank())

        hand = Hand.get_hand_from_cards(straight_from_2_to_4)
        self.assertEqual(HandType.STRAIGHT, hand.get_hand_type())
        self.assertEqual(Rank.FOUR, hand.get_hand_type_rank())

        hand = Hand.get_hand_from_cards(straight_ace_king_queen)
        self.assertEqual(HandType.STRAIGHT, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_type_rank())

    def test_pairs(self):
        hand = Hand.get_hand_from_cards(pair_of_7s_with_ace_high)
        self.assertEqual(HandType.PAIR, hand.get_hand_type())
        self.assertEqual(Rank.SEVEN, hand.get_hand_type_rank())
        self.assertEqual(Rank.ACE, hand.get_high_card_rank())

        hand = Hand.get_hand_from_cards(pair_of_aces_with_king_high)
        self.assertEqual(HandType.PAIR, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_type_rank())
        self.assertEqual(Rank.KING, hand.get_high_card_rank())

    def test_high_card(self):

        hand = Hand.get_hand_from_cards(seven_high)
        self.assertEqual(HandType.HIGH_CARD, hand.get_hand_type())
        self.assertEqual(Rank.SEVEN, hand.get_hand_type_rank())
        self.assertEqual(Rank.SEVEN, hand.get_high_card_rank())

        hand = Hand.get_hand_from_cards(ace_high_seven_kicker)
        self.assertEqual(HandType.HIGH_CARD, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_type_rank())
        self.assertEqual(Rank.ACE, hand.get_high_card_rank())

    def test_pre_check(self):
        self.assertRaisesRegex(ValueError, "Length of the cards need to be 3, given: 0 cards",
                               Hand.get_hand_from_cards, [])
        self.assertRaisesRegex(ValueError, "Length of the cards need to be 3, given: 2 cards",
                               Hand.get_hand_from_cards, [_TWO_OF_SPADES, _ACE_OF_SPADES])

    def test_sort_hands(self):
        hand_1 = Hand.get_hand_from_cards(set_of_aces)
        hand_2 = Hand.get_hand_from_cards(set_of_sevens)
        hand_3 = Hand.get_hand_from_cards(straight_from_2_to_4)
        hand_4 = Hand.get_hand_from_cards(straight_from_1_to_3)
        unsorted_hands = [hand_2, hand_4, hand_3, hand_1]
        self.assertEqual([hand_1, hand_2, hand_3, hand_4], Hand.sort_hands(unsorted_hands))

        hand_5 = Hand.get_hand_from_cards(straight_ace_king_queen)
        hand_6 = Hand.get_hand_from_cards(pair_of_aces_with_king_high)
        hand_7 = Hand.get_hand_from_cards(pair_of_7s_with_ace_high)
        hand_8 = Hand.get_hand_from_cards(ace_high_seven_kicker)
        unsorted_hands = [hand_8, hand_7, hand_6, hand_5]
        self.assertEqual([hand_5, hand_6, hand_7, hand_8], Hand.sort_hands(unsorted_hands))

        hand_9 = Hand.get_hand_from_cards(ace_high_four_kicker)
        hand_10 = Hand.get_hand_from_cards(seven_high)
        unsorted_hands = [hand_9, hand_10, hand_8]
        sorted_hands = Hand.sort_hands(unsorted_hands)
        self.assertEqual([hand_8, hand_9, hand_10], sorted_hands)


if __name__ == '__main__':
    unittest.main()
