class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = [0] + list(accumulate(nums, add))
        sumCounter = Counter(prefixSum)

        if goal == 0:
            return sum([n * (n - 1) // 2 for n in sumCounter.values()])

        return sum([sumCounter[i] * sumCounter[i - goal] for i in sumCounter.keys()])
