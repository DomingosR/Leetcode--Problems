class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        modVal = num % 9
        return modVal if modVal else 9