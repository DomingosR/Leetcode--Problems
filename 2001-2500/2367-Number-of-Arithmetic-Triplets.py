class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        numsSet = set()
        countTriplets = 0
        
        for num in nums:
            if num >= 2 * diff and (num - diff) in numsSet and (num - 2 * diff) in numsSet:
                countTriplets += 1
            numsSet.add(num)
            
        return countTriplets