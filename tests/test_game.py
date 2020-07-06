import unittest
from unittest import TestCase
from unittest.mock import patch
from game import Game
from deck import Deck
from hand import Hand, HandType
from card import Rank
from player import Player
from tests.utils import (
    _ACE_OF_SPADES,
    _ACE_OF_CLUBS,
    _KING_OF_CLUBS,
    _QUEEN_OF_CLUBS,
    _SEVEN_OF_CLUBS,
    _THREE_OF_CLUBS,
    _ACE_OF_HEARTS,
    _SEVEN_OF_HEARTS,
    _FOUR_OF_HEARTS,
    _TWO_OF_HEARTS,
    _ACE_OF_DIAMONDS,
    _JACK_OF_DIAMONDS,
    _KING_OF_DIAMONDS,
    _QUEEN_OF_DIAMONDS
)

_PLAYER_1 = Player("Player 1")
_PLAYER_2 = Player("Player 2")


def mock_process_tie_game(self, hands) -> Player:
    return _PLAYER_2


class TestGame(TestCase):
    def test_deal_hand(self):
        mocked_deck = Deck()
        mocked_deck._cards = list(reversed([_ACE_OF_HEARTS, _ACE_OF_SPADES, _ACE_OF_HEARTS,
                                            _ACE_OF_CLUBS, _SEVEN_OF_HEARTS, _SEVEN_OF_CLUBS]))
        game = Game(mocked_deck)
        hand = game._deal_hand()
        self.assertEqual(HandType.SET, hand.get_hand_type())
        self.assertEqual(Rank.ACE, hand.get_hand_type_rank())

        hand = game._deal_hand()
        self.assertEqual(HandType.PAIR, hand.get_hand_type())
        self.assertEqual(Rank.SEVEN, hand.get_hand_type_rank())
        self.assertEqual(Rank.ACE, hand.get_high_card_rank())

    @patch("game.Game._process_tie_game", mock_process_tie_game)
    def test_process_hands(self):
        game = Game()
        _set_of_aces = [_ACE_OF_HEARTS, _ACE_OF_SPADES, _ACE_OF_HEARTS]
        _pair_of_aces = [_ACE_OF_HEARTS, _ACE_OF_SPADES, _KING_OF_CLUBS]
        game._hand_to_player = {
            Hand(_set_of_aces, HandType.SET, Rank.ACE, Rank.ACE): _PLAYER_1,
            Hand(_pair_of_aces, HandType.PAIR, Rank.ACE, Rank.ACE): _PLAYER_2,
        }
        game._players = game._hand_to_player.values()
        self.assertEqual(_PLAYER_1, game._process_hands())

        _ace_high = [_ACE_OF_HEARTS, _FOUR_OF_HEARTS, _KING_OF_CLUBS]
        _pair_of_sevens = [_SEVEN_OF_CLUBS, _SEVEN_OF_HEARTS, _KING_OF_CLUBS]
        game._hand_to_player = {
            Hand(_pair_of_aces, HandType.HIGH_CARD, Rank.ACE, Rank.ACE): _PLAYER_1,
            Hand(_pair_of_sevens, HandType.PAIR, Rank.SEVEN, Rank.ACE): _PLAYER_2,
        }
        self.assertEqual(_PLAYER_2, game._process_hands())

        game._hand_to_player = {
            Hand([_ACE_OF_HEARTS, _KING_OF_CLUBS, _TWO_OF_HEARTS], HandType.HIGH_CARD, Rank.ACE, Rank.ACE): _PLAYER_1,
            Hand([_ACE_OF_CLUBS, _SEVEN_OF_HEARTS, _FOUR_OF_HEARTS], HandType.HIGH_CARD, Rank.ACE, Rank.ACE): _PLAYER_2,
        }
        self.assertEqual(_PLAYER_1, game._process_hands())

        game._hand_to_player = {
            Hand([_ACE_OF_HEARTS, _KING_OF_CLUBS, _ACE_OF_SPADES], HandType.PAIR, Rank.ACE, Rank.ACE): _PLAYER_1,
            Hand([_ACE_OF_CLUBS, _KING_OF_DIAMONDS, _ACE_OF_DIAMONDS], HandType.PAIR, Rank.ACE, Rank.ACE): _PLAYER_2,
        }
        self.assertEqual(_PLAYER_2, game._process_hands())

    def test_process_tie_game(self):
        deck = Deck()
        deck._cards.extend(list(reversed([
            _QUEEN_OF_CLUBS,  # player 1
            _JACK_OF_DIAMONDS  # player 2
        ])))
        game = Game(deck)
        game._hand_to_player = {
            Hand([_ACE_OF_HEARTS, _KING_OF_CLUBS, _ACE_OF_SPADES], HandType.PAIR, Rank.ACE, Rank.ACE): _PLAYER_1,
            Hand([_ACE_OF_CLUBS, _KING_OF_DIAMONDS, _ACE_OF_DIAMONDS], HandType.PAIR, Rank.ACE, Rank.ACE): _PLAYER_2,
        }
        game._players = game._hand_to_player.keys()

        self.assertEqual(_PLAYER_1, game._process_hands())

        deck._cards.extend(list(reversed([
            _QUEEN_OF_CLUBS,  # player 1
            _QUEEN_OF_DIAMONDS,  # player 2
            _THREE_OF_CLUBS,  # player 1
            _JACK_OF_DIAMONDS  # player 2
        ])))

        self.assertEqual(_PLAYER_2, game._process_hands())


if __name__ == "__main__":
    unittest.main()
