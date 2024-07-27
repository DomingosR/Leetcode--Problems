class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        leftTime = max(left) if left else -1
        rightTime = n - min(right) if right else -1
        return max(leftTime, rightTime)
        