class Solution(object):
    def wiggleSort(self, nums):
        n = len(nums)
        nums.sort()
        firstHalf, secondHalf = nums[:(n+1)//2], nums[(n+1)//2:]
        nums[::2] = firstHalf[::-1]
        nums[1::2] = secondHalf[::-1]
        return nums