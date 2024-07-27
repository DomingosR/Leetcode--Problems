class Solution(object):
    def findDisappearedNumbers(self, nums):
        allNums = set(range(1, len(nums)+1))

        for num in nums:
            allNums.discard(num)

        return list(allNums)