class Solution(object):
    def prefixCount(self, words, pref):
        return sum([1 for word in words if word[:len(pref)] == pref])
