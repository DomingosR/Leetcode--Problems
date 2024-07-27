class Solution(object):
    def uniqueOccurrences(self, arr):
        counterNums = Counter(arr)
        counterVals = Counter(counterNums.values())
        return max(counterVals.values()) <= 1
