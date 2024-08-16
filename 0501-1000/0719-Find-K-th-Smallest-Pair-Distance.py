class Solution(object):
    def smallestDistancePair(self, nums, k):
        n = len(nums)
        nums.sort()
        
        def countPairs(m):
            count = 0
            i, j = 0, 1
            while j < n:
                while i < j and nums[j] - nums[i] > m:
                    i += 1
                count += (j - i)
                j += 1
            
            return count
        
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = low + (high - low) // 2
            if countPairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low