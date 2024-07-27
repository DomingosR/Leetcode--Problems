def lenSequence(nums):
    if not nums:
        return 0
    
    values = set(nums)
    maxLen = 1
    
    for i in values:
        if i-1 in values:
            continue
        currentLen = 1
        while i+1 in values:
            currentLen += 1
            i += 1
        maxLen = max(maxLen, currentLen)
    
    return maxLen

class Solution(object):
    def longestConsecutive(self, nums):
        return lenSequence(nums)