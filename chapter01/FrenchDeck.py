import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    def __setitem__(self, position, card):
        self._cards[position] = card
if __name__ == "__main__":
    fd = FrenchDeck()
    #for indx in range(len(fd)):
    #    print(fd.__getitem__(indx))
    for card in sorted(fd, key=spades_high):
        print(card)
