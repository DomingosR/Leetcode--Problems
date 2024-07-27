class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        accum1 = [0] + list(accumulate(nums))
        accum2 = [0] + list(accumulate(reversed(nums)))
        
        leftDiff = [i * nums[i] - accum1[i] for i in range(n)]
        rightDiff = [-i * nums[-i-1] + accum2[i] for i in range(n)][::-1]
        
        return [leftDiff[i] + rightDiff[i] for i in range(n)]