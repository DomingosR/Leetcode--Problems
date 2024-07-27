class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        currentVal = k

        for num in nums:
            currentVal ^= num

        return currentVal.bit_count()
