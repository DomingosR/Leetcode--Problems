class Solution(object):
    def canTraverseAllPairs(self, nums):
        def gcd(m, n):
            while m % n > 0:
                m, n = n, m % n
            return n
        
        if len(nums) == 1:
            return True
        
        if 1 in nums: 
            return False
        
        nums = sorted(set(nums), reverse = True)
        n = len(nums)
        if n == 1:
            return True

        for i in range(n-1):
            j = i+1
            for j in range(i+1, n):
                div = gcd(nums[i], nums[j])
                if div > 1:
                    nums[j] *= (nums[i] // div)
                    break
            else:                                   # Note: this isn't executed if the loop breaks
                return False

        return True 