class Solution(object):
    def shortestSequence(self, rolls, k):
        n = len(rolls)
        diceRolls = set()
        length = 0

        for i in range(n):
            diceRolls.add(rolls[i])
            if len(diceRolls) == k:
                length += 1
                diceRolls = set()
        
        return (length + 1)
