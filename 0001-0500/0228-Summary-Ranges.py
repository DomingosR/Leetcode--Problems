class Solution(object):
    def summaryRanges(self, nums):
        n = len(nums)
        
        if n == 0: return []
        if n == 1: return [str(nums[0])]
        
        currentIndex = 0
        sortedRanges = []
        
        while currentIndex < n:
            nextIndex = currentIndex
            while nextIndex < n-1 and nums[nextIndex + 1] == nums[nextIndex] + 1:
                nextIndex += 1
            if nextIndex == currentIndex:
                sortedRanges.append(str(nums[currentIndex]))
                currentIndex += 1
            else:
                auxStr = str(nums[currentIndex]) + "->" + str(nums[nextIndex])
                sortedRanges.append(auxStr)
            currentIndex = nextIndex + 1
        
        return sortedRanges