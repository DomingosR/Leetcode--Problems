class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck = sorted(deck)[::-1]

        cardDeque = deque()

        for num in deck:
            if cardDeque:
                cardDeque.appendleft(cardDeque.pop())
            cardDeque.appendleft(num)

        return list(cardDeque)
