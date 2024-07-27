class Solution(object):
    def successfulPairs(self, spells, potions, success):
        n = len(potions)
        potions.sort()
        returnVal = []

        for i in range(len(spells)):
            minStrength = 1.0 * success / spells[i]
            returnVal.append(n - bisect_left(potions, minStrength))

        return returnVal