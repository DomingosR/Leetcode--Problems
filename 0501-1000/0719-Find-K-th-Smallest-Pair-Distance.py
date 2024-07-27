class Solution(object):
    def smallestDistancePair(self, nums, k):
        n = len(nums)
        nums.sort()
        
        def diffCount(threshold):
            i, j, count = 0, 0, 0
            while i < n:
                while j < n and nums[j] - nums[i] <= threshold:
                    j += 1
                count += j - i - 1
                i += 1
            return count
        
        minVal = 0
        maxVal = nums[-1] - nums[0]
        while minVal < maxVal:
            midVal = (minVal + maxVal) // 2
            if diffCount(midVal) < k:
                minVal = midVal + 1
            else:
                maxVal = midVal
        
        return minVal