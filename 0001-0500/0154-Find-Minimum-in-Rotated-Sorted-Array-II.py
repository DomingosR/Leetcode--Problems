class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        
        def findMinVal(lowIndex, highIndex):
            if lowIndex == highIndex:
                return nums[lowIndex]
            
            if highIndex - lowIndex == 1:
                return nums[lowIndex] if nums[lowIndex] < nums[highIndex] else nums[highIndex]
            
            midIndex = lowIndex + (highIndex - lowIndex) // 2
            val1, val2, val3 = nums[midIndex - 1], nums[midIndex], nums[midIndex + 1]
            
            if val1 > val2:
                return val2
            
            if val2 > val3:
                return val3
            
            if val3 > nums[highIndex]:
                return findMinVal(min(midIndex + 1, highIndex), highIndex)
                
            if val1 < nums[lowIndex]:
                return findMinVal(lowIndex, midIndex - 1)
            
            return min(findMinVal(lowIndex, midIndex - 1), findMinVal(min(midIndex + 1, highIndex), highIndex))
        
        return findMinVal(0, len(nums) - 1)