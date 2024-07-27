class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return [candy >= (max(candies) - extraCandies) for candy in candies]