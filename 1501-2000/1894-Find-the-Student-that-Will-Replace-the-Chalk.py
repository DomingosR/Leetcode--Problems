class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        currentSum = list(accumulate(chalk))
        totalChalk = currentSum[-1]
        
        k %= totalChalk
        return bisect_right(currentSum, k)    