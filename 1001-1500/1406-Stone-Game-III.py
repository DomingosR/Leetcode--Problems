class Solution(object):
    def stoneGameIII(self, stoneValue):
        numStones = len(stoneValue)
        optimalValues = [0] * 3

        for i in range(numStones - 1, -1, -1):
            optimalValues[i % 3] = max(sum(stoneValue[i:i + k]) - optimalValues[(i + k) % 3] for k in (1, 2, 3))
        return ["Tie", "Alice", "Bob"][cmp(optimalValues[0], 0)]
