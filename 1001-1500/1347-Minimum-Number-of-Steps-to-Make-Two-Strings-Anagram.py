class Solution(object):
    def minSteps(self, s, t):
        return sum([v for v in (Counter(s) - Counter(t)).values() if v > 0])