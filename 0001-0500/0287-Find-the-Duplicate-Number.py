class Solution(object):
    def findDuplicate(self, nums):
        slowPointer = nums[0]
        fastPointer = nums[nums[0]]
        
        while slowPointer != fastPointer:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]
            
        fastPointer = 0
        
        while slowPointer != fastPointer:
            slowPointer = nums[slowPointer]
            fastPointer = nums[fastPointer]
            
        return slowPointer