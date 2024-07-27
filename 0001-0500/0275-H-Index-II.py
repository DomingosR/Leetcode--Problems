class Solution(object):
    def hIndex(self, citations):
        if citations[-1] == 0:
            return 0
        
        n = len(citations)
        lowIndex, highIndex = 0, n - 1
        
        while lowIndex < highIndex:
            midIndex = lowIndex + (highIndex - lowIndex) // 2
            if citations[midIndex] >= n - midIndex:
                highIndex = midIndex
            else:
                lowIndex = midIndex + 1
                
        return n - lowIndex
