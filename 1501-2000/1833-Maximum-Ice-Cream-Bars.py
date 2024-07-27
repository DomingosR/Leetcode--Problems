class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        totalCost = list(accumulate(sorted(costs)))
        return bisect_right(totalCost, coins)     