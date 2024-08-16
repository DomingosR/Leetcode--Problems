class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        occurrences = []
        for i, num in enumerate(nums):
            if num == x:
                occurrences.append(i)
                
        indices = []
        
        for index in queries:
            indices.append(occurrences[index - 1] if index <= len(occurrences) else -1)
            
        return indices