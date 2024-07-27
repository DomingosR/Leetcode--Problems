class Solution(object):
    def numSubseq(self, nums, target):
        p = 10**9 + 7
        nums.sort()
        n = len(nums)
        
        i, j = 0, n-1
        countSubseq = 0
        
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                countSubseq += 2**(j-i)
                i += 1
            
        return countSubseq % p