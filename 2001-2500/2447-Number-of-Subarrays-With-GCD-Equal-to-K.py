class Solution(object):
    def subarrayGCD(self, nums, k):
        def gcd(m, n):
            while n:
                m, n = n, m % n
            return m
        
        numArrays = 0
        
        for i in range(len(nums)):
            currentVal = nums[i]
            if currentVal == k:
                numArrays += 1
            j = i + 1
            while currentVal % k == 0 and j < len(nums):
                currentVal = gcd(currentVal, nums[j])  
                if currentVal == k:
                    numArrays += 1
                j += 1
                    
        return numArrays