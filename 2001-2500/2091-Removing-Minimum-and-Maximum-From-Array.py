class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        
        minIndex, maxIndex = nums.index(min(nums)), nums.index(max(nums))
        if minIndex > maxIndex:
            minIndex, maxIndex = maxIndex, minIndex
        
        if minIndex + 1 < n - maxIndex:
            numDeletions = min(n - (maxIndex - minIndex) + 1 , maxIndex + 1)
        else:
            numDeletions = min(n - (maxIndex - minIndex) + 1, n - minIndex)
            
        return numDeletions