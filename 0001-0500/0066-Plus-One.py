class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        digits.reverse()

        i = 0
        while i < n and digits[i] == 9:
            digits[i] = 0
            i += 1
        
        if i == n:
            digits.append(1)
        else:
            digits[i] += 1
        
        digits.reverse()
        return digits