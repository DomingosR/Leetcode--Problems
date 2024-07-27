class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False
        
        cardCounter = Counter(hand)
        
        for card in sorted(cardCounter):
            while cardCounter[card] > 0:
                for i in range(groupSize):
                    cardCounter[card + i] -= 1
                    if cardCounter[card + i] < 0:
                        return False
                    
        return True