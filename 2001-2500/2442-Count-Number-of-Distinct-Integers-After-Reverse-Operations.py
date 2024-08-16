class Solution(object):
    def countDistinctIntegers(self, nums):
        numsSet = set(nums)
        finalSet = set()
        
        for num in numsSet:
            finalSet.add(num)
            finalSet.add(int(str(num)[::-1]))
        
        return len(finalSet)