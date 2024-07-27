class Solution(object):
    def singleNumber(self, nums):
        XOR1 = 0
        
        for num in nums:
            XOR1 ^= num
        
        for bit in range(32):
            if XOR1 & (1 << bit):
                firstSetBit = (1 << bit)
                break
        
        XOR2 = 0
        for num in nums:
            if num & firstSetBit:
                XOR2 ^= num
                
        return [XOR2, XOR1 ^ XOR2]