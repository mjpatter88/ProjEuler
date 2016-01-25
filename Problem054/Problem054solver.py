# Python 3
from enum import IntEnum

class Rank(IntEnum):
    """
    """
    high_card = 0
    one_pair = 1
    two_pair = 2
    three_of_a_kind = 3
    straight = 4
    flush = 5
    full house = 6
    four_of_a_kind = 7
    straight_flush = 8
    royal_flusH = 9


class Card():
    """
    """
    def __init__(self, card_string):
        """
        """
        pass


class PokerHand():
    """
    """
    def __init__(self, hands):
        """
        """
        assert len(hands) == 5, "You must supply 5 cards. You supplied {0} cards.".format(len(hands))

    def rank(self):
        """
        """
        pass

    def value(self):
        """
        """
        pass

# https://docs.python.org/3/reference/datamodel.html#object.__lt__

    def __eq__(self, other):
        """
        """
        pass

    def __lt__(self, other):
        """
        """
        pass

    def __gt__(self, other):
        """
        """
        pass


if __name__ == '__main__':
    with open('poker.txt') as input_file:
        for line in input_file:
            player1_hand = PokerHand(line.split(" ")[:5])
            player2_hand = PokerHand(line.split(" ")[5:])

