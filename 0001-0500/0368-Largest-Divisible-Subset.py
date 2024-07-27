class Solution(object):
    def largestDivisibleSubset(self, nums):
        nums.sort()

        chain = [(-1, 1)]
        overallMaxLen, startChain = 1, 0

        for i in range(1, len(nums)):
            maxLen, prev = 1, -1
            for j in range(i):
                if nums[i] % nums[j] == 0 and chain[j][1] >= maxLen:
                    maxLen, prev = chain[j][1] + 1, j
            if maxLen > overallMaxLen:
                overallMaxLen, startChain = maxLen, i
            chain.append((prev, maxLen))

        maximalChain, currentIndex = [], startChain

        while currentIndex >= 0:
            maximalChain.append(nums[currentIndex])
            currentIndex = chain[currentIndex][0]

        return maximalChain[::-1]
            
