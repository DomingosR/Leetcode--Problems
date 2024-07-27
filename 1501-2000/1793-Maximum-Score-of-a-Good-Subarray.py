class Solution(object):
    def maximumScore(self, nums, k):
        n = len(nums)
        maxScore, minVal = nums[k], nums[k]
        i, j = k, k

        while i > 0 or j < n-1:
            if (nums[i-1] if i else 0) < (nums[j+1] if j < n-1 else 0):
                j += 1
                minVal = min(minVal, nums[j])
            else:
                i -= 1
                minVal = min(minVal, nums[i])
            maxScore = max(maxScore, minVal * (j-i+1))
        
        return maxScore