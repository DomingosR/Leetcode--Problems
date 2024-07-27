class Solution(object):
    def PredictTheWinner(self, nums):
        preComputed = {}

        def value(i, j):
            if (i, j) not in preComputed:
                if i == j:
                    preComputed[(i, i)] = nums[i]
                else:
                    val1 = nums[i] - value(i+1, j)
                    val2 = nums[j] - value(i, j-1)
                    preComputed[(i, j)] = max(val1, val2)

            return preComputed[(i, j)]

        return value(0, len(nums) - 1) >= 0
