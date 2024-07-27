class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)
        if not total % 3:
            return total
        
        numsMod1 = sorted([num for num in nums if num % 3 == 1])
        numsMod2 = sorted([num for num in nums if num % 3 == 2])
        
        if total % 3 == 1:
            if numsMod1 and len(numsMod2) >= 2:
                return total - min(numsMod1[0], sum(numsMod2[:2]))
            if numsMod1:
                return total - numsMod1[0]
            else:
                return total - sum(numsMod2[:2])
                
        if total % 3 == 2:
            if numsMod2 and len(numsMod1) >= 2:
                return total - min(numsMod2[0], sum(numsMod1[:2]))
            if numsMod2:
                return total - numsMod2[0]
            else:
                return total - sum(numsMod1[:2])