class Solution(object):
    def maxFrequencyElements(self, nums):
        numCounter = Counter(nums)
        maxFreq = max(numCounter.values())
        freqCounter = Counter(numCounter.values())
        return maxFreq * freqCounter[maxFreq]
        
