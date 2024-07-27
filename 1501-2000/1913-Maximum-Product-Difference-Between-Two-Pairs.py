class Solution(object):
    def maxProductDifference(self, nums):
        large1, large2 = 0, 0
        small1, small2 = 10001, 10001

        for n in nums:
            if n >= large1:
                large1, large2 = n, large1
            elif n > large2:
                large2 = n

            if n <= small1:
                small1, small2 = n, small1
            elif n < small2:
                small2 = n

        return large1 * large2 - small1 * small2
