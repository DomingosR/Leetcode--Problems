class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        if k == 0:
            return 1
        
        bitCount = [0] * 6
        minLen = 100
        
        def currentNum():
            return sum([(1 << i) * (1 if bitCount[i] > 0 else 0) for i in range(6)])
    
        rightEnd, leftEnd = 0, 0
        
        while rightEnd < len(nums):
            while rightEnd < len(nums) and currentNum() < k:
                for i in range(6):
                    bitCount[i] += (nums[rightEnd] >> i) & 1
                rightEnd += 1
                
            if currentNum() >= k:
                while leftEnd < rightEnd and currentNum() >= k:
                    for i in range(6):
                        bitCount[i] -= (nums[leftEnd] >> i) & 1
                    leftEnd += 1   
                    
                minLen = min(minLen, rightEnd - leftEnd + 1)
                
        return -1 if minLen == 100 else minLen