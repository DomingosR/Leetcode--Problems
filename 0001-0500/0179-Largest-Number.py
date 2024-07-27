class Solution(object):
    def largestNumber(self, nums):
        def compNums(str1, str2):
            if str1 + str2 > str2 + str1: return 1
            if str1 == str2: return 0
            return -1
        
        auxNums = [str(num) for num in nums]
        auxNums.sort(cmp = lambda str1, str2: compNums(str1, str2), reverse = True)
        return ''.join(auxNums).lstrip('0') or '0'