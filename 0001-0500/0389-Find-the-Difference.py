class Solution(object):
    def findTheDifference(self, s, t):
        countS, countT = Counter(s), Counter(t)
        diffCount = countT - countS
        return [c for c in diffCount if diffCount[c] == 1][0]