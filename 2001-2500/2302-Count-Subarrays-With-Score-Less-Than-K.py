def findNumArrays(nums, k):
    countNums = len(nums)
    numArrays = 0
    left = 0
    currentSum = 0
    
    for right in range(countNums):
        currentSum += nums[right]
        while left <= right and (right-left+1)*currentSum >= k:
            currentSum -= nums[left]
            left += 1
        numArrays += (right-left+1)    
    
    return numArrays

class Solution(object):
    def countSubarrays(self, nums, k):
        return findNumArrays(nums, k)