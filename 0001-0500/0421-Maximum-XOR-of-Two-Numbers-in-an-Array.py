class Solution(object):
    def findMaximumXOR(self, nums):
        maxXOR = 0
        
        for i in range(31)[::-1]:
            maxXOR <<= 1
            prefixes = {num >> i for num in nums}
            maxXOR += any(maxXOR ^ pref ^ 1 in prefixes for pref in prefixes)
        
        return maxXOR