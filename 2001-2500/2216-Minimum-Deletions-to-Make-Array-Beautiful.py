class Solution(object):
    def minDeletion(self, nums):
        numDeletions = 0
        prevElement = -1
        
        for num in nums:
            if num == prevElement:
                numDeletions += 1
            else:
                prevElement = num if prevElement < 0 else -1
        
        return numDeletions + (prevElement >= 0)