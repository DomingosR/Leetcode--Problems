class Solution(object):
    def makeEqual(self, words):
        n = len(words)
        combinedStr = "".join(words)
        letterCounter = Counter(combinedStr)
        return all([val % n == 0 for val in letterCounter.values()])
