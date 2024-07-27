def maxLength(nums):
    if len(nums) == 1:
        return 1

    i = 1
    while i < len(nums):
        deleteElement = False
        if nums[i] == nums[i-1]: deleteElement = True
        if (i < len(nums) - 1) and (nums[i] - nums[i-1]) * (nums[i+1] - nums[i]) >= 0: deleteElement = True

        if deleteElement:
            del nums[i]
        else:
            i += 1

    return len(nums)

class Solution(object):
    def wiggleMaxLength(self, nums):
        return maxLength(nums)
