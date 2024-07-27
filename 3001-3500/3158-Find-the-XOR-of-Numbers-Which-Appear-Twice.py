class Solution(object):
    def duplicateNumbersXOR(self, nums):
        XOR = 0
        seenNumbers = set()
        
        for num in nums:
            if num in seenNumbers:
                XOR ^= num
            else:
                seenNumbers.add(num)
                
        return XOR