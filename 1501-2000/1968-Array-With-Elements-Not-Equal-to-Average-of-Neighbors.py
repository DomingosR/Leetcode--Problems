class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        n = len(nums)
        i, j, reordered = 0, (n+1) // 2, []
        
        while i < (n+1) // 2:
            reordered.append(nums[i])
            if j < n:
                reordered.append(nums[j])
            i += 1
            j += 1
        
        return reordered