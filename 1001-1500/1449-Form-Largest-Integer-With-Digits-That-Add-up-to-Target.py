class Solution(object):
    def largestNumber(self, cost, target):
        maxNumberForCost = [0] + [-1] * target

        for n in range(1, target + 1):
            auxArray = [10 * maxNumberForCost[n - c] + (digit + 1) for digit, c in enumerate(cost) if c <= n]
            if auxArray:
                maxNumberForCost[n] = max(auxArray)

        return str(max(maxNumberForCost[target], 0))
