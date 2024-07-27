class Solution(object):
    def sortArrayByParity(self, nums):
        evenNums = [i for i in nums if i % 2 == 0]
        oddNums = [i for i in nums if i % 2 == 1]
        return evenNums + oddNums
