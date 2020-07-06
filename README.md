# Drunk Poken

The festival season is here and you realise it's hard to play all those complicated card games when you're drunk.
You decide to create a simple luck-based game for people to play when they have limited motor and sensory control.

Basic Rules:
- Use a standard deck of cards (no Joker).
- Each player is dealt only three cards.
- 'A' is considered to have a number value of 1.
- 'A' is considered the top card in a face-off. So the order is A > K > Q > J > 10...2

Victory:
- A trail (three cards of the same number) is the highest possible combination.
- The next highest is a sequence (numbers in order, e.g., 4,5,6. A is considered to have a value of 1).
- The next highest is a pair of cards (e.g.: two Kings or two 10s).
- If all else fails, the top card (by number value wins).
- If the top card has the same value, each of the tied players draws a single card from the deck until a winner is found.
- Only the newly drawn cards are compared to decide a tie. The top card wins a tie.
- For now the suit (spades/hearts etc...), does not matter.

PRE-REQUISITES
--------------
1. Need Python 3.6


*RUNNING TESTS:*
------
### Install nose lib:
```bash
  pip install nose
```
OR
```bash
  pip install -r test-requirements.txt
```

### To run all tests at once:
```bash
  nosetests .
```


*TO RUN THE GAME:*
------
```bash
  python3 main.py
```

