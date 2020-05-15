# Date:2020/5/15
# Author:Lingchen
# Mark: 一摞Python风格的纸牌
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    纸牌对象类
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """
        初期化纸牌
        """
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        """
        返回纸牌数量
        :return:
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        抽取纸牌
        :param position:
        :return:
        """
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print('beer_card: ', beer_card)

deck = FrenchDeck()
print('Len of deck: ', len(deck))

print('deck[0]: ', deck[0])
print('deck[-1]: ', deck[-1])

# 随机抽取一张纸牌
print('choice 1: ', choice(deck))
print('choice 2: ', choice(deck))
print('choice 3: ', choice(deck))

# 查看纸牌切片操作
print('deck slice: ', deck[:3])
print('deck A: ', deck[12::13])

# 迭代纸牌
for card in deck:
    print('deck: ', card)

# 反向迭代纸牌
for card in reversed(deck):
    print('deck reversed: ', card)

# in运算符就会按顺序做一次迭代搜索
print('In operate: ', Card('Q', 'hearts') in deck)
print('In operate: ', Card('7', 'beats') in deck)

# 按照常规，用点数来判定扑克牌的大小，2最小，A最大
# 花色的大小: 黑桃最大、红桃次之、方块再次、梅花最小。
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    """
    给出扑克牌排序（大小）的函数
    :param card:
    :return:
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print('sorted: ', card)

