class Solution(object):
    def majorityElement(self, nums):
        candidate, count = -10**9 -  1, 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            else:
                count += (1 if candidate == num else -1)
                
        return candidate