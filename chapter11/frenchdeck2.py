import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        print('__init__')
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        print('__len__')
        return len(self._cards)
    def __getitem__(self, position):
        print('__getitem__')
        return self._cards[position]
    def __setitem__(self, position, value):
        print('__setitem__')
        self._cards[position] = value
    def __delitem__(self, position):
        print('__delitem__')
        del self._cards[position]
    def insert(self, position, value):
        print('insert')
        self._cards.insert(position, value)
