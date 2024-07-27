class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        def isArithmetic(startIndex, endIndex):
            numSet = set(nums[startIndex:endIndex + 1])
            minVal = min(numSet)
            maxVal = max(numSet)
            
            if minVal == maxVal:
                return True
            
            count = len(numSet)
            if count < endIndex - startIndex + 1:
                return False
            
            if (maxVal - minVal) % (count - 1) != 0:
                return False
            
            interval = (maxVal - minVal) // (count - 1)
            
            for i in range(count):
                if not (minVal + i * interval in numSet):
                    return False
            
            return True
        
        return [isArithmetic(startIndex, endIndex) for startIndex, endIndex in zip(l, r)]