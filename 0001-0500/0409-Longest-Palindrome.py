class Solution(object):
    def longestPalindrome(self, s):
        letterCounter = Counter(s)
        numPairs = [ (i // 2) for i in letterCounter.values()]
        oddNums = [i for i in letterCounter.values() if i % 2 == 1]
        isThereOdd = 1 if len(oddNums) > 0 else 0

        return  2 * sum(numPairs) + isThereOdd