class Solution(object):
    def totalMoney(self, n):
        q = n // 7
        r = n - 7 * q
        
        amount = 28 * q + q * (q - 1) * 7 // 2
        if r > 0:
            amount += r * (2 * q + r + 1) // 2
        return amount