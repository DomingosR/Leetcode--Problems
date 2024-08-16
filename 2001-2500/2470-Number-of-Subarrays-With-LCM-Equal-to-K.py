class Solution(object):
    def subarrayLCM(self, nums, k):
        def lcm(m, n):
            return (m // gcd(m, n)) * n
        
        def gcd(m, n):
            while n:
                m, n = n, m % n
            return m
        
        numArrays = 0
        
        for i in range(len(nums)):
            currentVal = 1
            for j in range(i, len(nums)):
                currentVal = lcm(currentVal, nums[j])
                if currentVal == k:
                    numArrays += 1
                if currentVal > k or k % currentVal:
                    break
                    
        return numArrays