class Solution(object):
    def checkValidString(self, s):
        countMax, countMin = 0, 0

        for char in s:
            if char == "(":
                countMax += 1
                countMin += 1
            if char == ")":
                countMax -= 1
                countMin = max(countMin - 1, 0)
            if char == "*":
                countMax += 1
                countMin = max(countMin - 1, 0)
            if countMax < 0:
                return False

        return countMin == 0
