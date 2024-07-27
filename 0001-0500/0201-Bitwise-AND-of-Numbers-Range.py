class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        i = 0
        while left != right:
            i += 1
            left >>= 1
            right >>= 1
        return left << i