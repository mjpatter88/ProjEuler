# Python 3

class PokerHand():
    def __init__(self, hands):
        assert len(hands) == 5, "You must supply 5 cards. You supplied {0} cards.".format(len(hands))

if __name__ == '__main__':
    with open('poker.txt') as input_file:
        for line in input_file:
            player1_hand = PokerHand(line.split(" ")[:5])
            player2_hand = PokerHand(line.split(" ")[5:])

