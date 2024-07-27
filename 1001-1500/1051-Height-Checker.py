class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        comparison = list(map(list, zip(heights, sorted(heights))))
        return sum([pair[0] != pair[1] for pair in comparison])