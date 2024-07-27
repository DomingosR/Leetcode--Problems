class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cumSum = list(accumulate(nums))
        cumSumMod = [0] + [indNum % k for indNum in cumSum]
        modCounter = Counter(cumSumMod)

        return sum([n*(n-1)//2 for n in modCounter.values()])  