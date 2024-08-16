class Solution(object):
    def arrayChange(self, nums, operations):
        substitutions = defaultdict(int)
        
        for u, v in reversed(operations):
            substitutions[u] = (substitutions[v] if v in substitutions else v)
        
        for i, num in enumerate(nums):
            if num in substitutions:
                nums[i] = substitutions[num]
                
        return nums