class Solution(object):
    def countQuadruplets(self, nums):
        n = len(nums)
        count = 0
        sumCount = defaultdict(int)

        for x in range(1, n-1):
            c = x
            for d in range(c+1, n):
                count += sumCount[nums[d] - nums[c]]
            b = x
            for a in range(b):
                sumCount[nums[a] + nums[b]] += 1

        return count
