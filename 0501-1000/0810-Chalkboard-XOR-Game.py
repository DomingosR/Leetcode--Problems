class Solution(object):
    def xorGame(self, nums):
        overall = reduce(xor, nums)
        if overall == 0:
            return True
        
        return len(nums) % 2 == 0