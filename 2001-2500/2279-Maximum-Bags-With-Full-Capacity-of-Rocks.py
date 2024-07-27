class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        spareCapacity = [capacity[i] - rocks[i] for i in range(n)]
        spareCapacity.sort()
        cumSpare = list(accumulate(spareCapacity))

        return bisect_right(cumSpare, additionalRocks)        