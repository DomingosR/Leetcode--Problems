class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        lowVal = -10**9-1
        n = len(nums)
        valueStack = [lowVal]
        thirdNum = lowVal

        for i in range(n-1, -1, -1):
            if nums[i] < thirdNum:
                return True
            while valueStack and valueStack[-1] < nums[i]:
                thirdNum = valueStack.pop()
            valueStack.append(nums[i])

        return False
